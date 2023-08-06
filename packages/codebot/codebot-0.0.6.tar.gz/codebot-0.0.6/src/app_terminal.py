import uuid
import openai
import json
import ast
import os
import chainlit as cl
from functions.FunctionManager import FunctionManager
import inspect
import tiktoken
import importlib
import asyncio
from get_text import get_text
import platform


# Path of the configuration file
config_path = os.path.join(os.path.expanduser('~'), '.codebot', 'config.json')

# Read the configuration file
with open(config_path, 'r') as config_file:
    config_env = json.load(config_file)

openai.api_key = config_env['openai']['api_key']
openai.api_base = config_env['openai']['api_base']

current_dir = os.path.dirname(os.path.abspath(__file__))
plugins_dir = os.path.join(current_dir, 'plugins')

plugin_dirs = [
    d for d in os.listdir(plugins_dir)
    if os.path.isdir(os.path.join(plugins_dir, d)) and d != '__pycache__'
]

functions = []
for dir in plugin_dirs:
    try:
        with open(f'plugins/{dir}/config.json', 'r') as f:
            config = json.load(f)
        enabled = config.get('enabled', True)
    except FileNotFoundError:
        enabled = True

    if not enabled:
        continue

    module = importlib.import_module(f'plugins.{dir}.functions')
    functions.extend([
        obj for name, obj in inspect.getmembers(module) if inspect.isfunction(obj)
    ])

function_manager = FunctionManager(functions=functions)
print("functions:", function_manager.generate_functions_array())
env_max_tokens = config_env['openai']['max_tokens']
if env_max_tokens is not None:
    max_tokens = int(env_max_tokens)
else:
    max_tokens = 5000
is_stop = False


def __truncate_conversation(conversation):
    system_con = conversation[0]
    conversation = conversation[1:]
    while True:
        if (get_token_count(conversation) > max_tokens and len(conversation) > 1):
            conversation.pop(1)
        else:
            break
    conversation.insert(0, system_con)
    return conversation


def get_token_count(conversation):
    encoding = tiktoken.encoding_for_model(config_env['openai']['model'])

    num_tokens = 0
    for message in conversation:
        num_tokens += 4
        for key, value in message.items():
            num_tokens += len(encoding.encode(str(value)))
            if key == "name":
                num_tokens += -1
    num_tokens += 2
    return num_tokens


MAX_ITER = 100


async def on_message(user_message: object):
    global is_stop
    is_stop = False
    print("==================================")
    print(user_message)
    print("==================================")
    user_message = str(user_message)
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": user_message})
    cur_iter = 0
    while cur_iter < MAX_ITER and not is_stop:

        openai_message = {"role": "", "content": ""}
        function_ui_message = None
        content_ui_message = cl.Message(content="")
        stream_resp = None
        send_message = __truncate_conversation(message_history)
        try:
            functions = function_manager.generate_functions_array()
            user_plugin_api_info = cl.user_session.get('user_plugin_api_info')
            if user_plugin_api_info is not None:
                for item in user_plugin_api_info:
                    for i in item['api_info']:
                        functions.append(i)
            print("functions:", functions)
            for stream_resp in openai.ChatCompletion.create(
                    model=config_env['openai']['model'],
                    messages=send_message,
                    stream=True,
                    function_call="auto",
                    functions=functions,
                    temperature=0):  # type: ignore
                new_delta = stream_resp.choices[0]["delta"]
                if is_stop:
                    is_stop = True
                    cur_iter = MAX_ITER
                    break
                openai_message, content_ui_message, function_ui_message = await process_new_delta(
                    new_delta, openai_message, content_ui_message, function_ui_message)
        except Exception as e:
            print(e)
            cur_iter += 1
            await asyncio.sleep(1)
            continue

        if stream_resp is None:
            await asyncio.sleep(2)
            continue

        if function_ui_message is not None:
            await function_ui_message.send()

        if stream_resp.choices[0]["finish_reason"] == "stop":
            break
        elif stream_resp.choices[0]["finish_reason"] != "function_call":
            raise ValueError(stream_resp.choices[0]["finish_reason"])

        function_name = openai_message.get("function_call").get("name")
        print(openai_message.get("function_call"))
        function_response = ""
        try:
            arguments = json.loads(
                openai_message.get("function_call").get("arguments"))
        except:
            try:
              arguments = ast.literal_eval(
                  openai_message.get("function_call").get("arguments"))
            except:
              if function_name == 'python' or function_name == 'python_exec':
                if function_name == 'python':
                  function_name = 'python_exec'
                arguments = {"code": openai_message.get("function_call").get("arguments")}
                openai_message["function_call"]["arguments"] = json.dumps(arguments)
        try:
            function_response = await function_manager.call_function(
                function_name, arguments)
        except Exception as e:
            print(e)
            raise e 
        print("==================================")
        print(function_response)
        if type(function_response) != str:
            function_response = str(function_response)
        
        message_history.append(openai_message)
        
        if function_name == 'python_exec' and 'status' in function_response and 'error_info' in function_response and 'error' in function_response:
            # function_response 中取出 description 并从中 去掉这个key
            print("🚀" * 20)
            function_response = json.loads(function_response)
            description = function_response['description']
            del function_response['description']
            message_history.append({
                "role": "function",
                "name": function_name,
                "content": json.dumps(function_response),
            })
            language = config_env['openai']['language']
            message_history.append({
                "role": "user",
                "content": str(description) + "\n\n" + "Please answer me in " + language
            })
            print("🚀" * 20)
        else:
            message_history.append({
                "role": "function",
                "name": function_name,
                "content": function_response,
            })
            
        print("==================================")
        print(message_history)
        print("==================================")

        await cl.Message(
            author=function_name,
            content=str(function_response),
            language="json",
            indent=1,
        ).send()
        cur_iter += 1


async def process_new_delta(new_delta, openai_message, content_ui_message,
                            function_ui_message):
    if "role" in new_delta:
        openai_message["role"] = new_delta["role"]
    if "content" in new_delta:
        new_content = new_delta.get("content") or ""
        openai_message["content"] += new_content
        await content_ui_message.stream_token(new_content)
    if "function_call" in new_delta:
        if "name" in new_delta["function_call"]:
            function_name = new_delta["function_call"]["name"]
            if function_name == "python":
                function_name = "python_exec"
            openai_message["function_call"] = {
                "name": function_name,
            }
            await content_ui_message.send()
            function_ui_message = cl.Message(
                author=function_name,
                content="",
                indent=1,
                language="json")
            await function_ui_message.stream_token(function_name)

        if "arguments" in new_delta["function_call"]:
            if "arguments" not in openai_message["function_call"]:
                openai_message["function_call"]["arguments"] = ""
            openai_message["function_call"]["arguments"] += new_delta[
                "function_call"]["arguments"]
            await function_ui_message.stream_token(
                new_delta["function_call"]["arguments"])
    return openai_message, content_ui_message, function_ui_message



@cl.on_chat_start
async def start_chat():
    password = config_env['openai']['password']
    platform_name = platform.system()
    content = '''You are a great terminal tool for {platform_name}, which can help users better execute {platform_name} terminal commands.
If you encounter a situation where the sudo command is required, you need to automatically input the password in the cmd instead of waiting for terminal input. 
No command should generate any terminal input.
The {platform_name} user name is luzhipeng and the password is "{password}" 
[IMPORTANT] You must judge for yourself whether you need to use sudo, not all commands should be used with sudo directly.
example:
if the command is "sudo apt-get install zerotier-cli", you need to change it to "echo '{password}' | sudo -S apt-get install zerotier-cli"
if the command does not need to be executed as root, you can directly execute the command,like "ls"    
the terminal function argumets like this:
```json
{{
    "cmd": "ls",
}}
```
'''.format(platform_name=platform_name, password=password)
    language = config_env['openai']['language']
    cl.user_session.set(
        "message_history",
        [{
            "role":
            "system",
            "content": content + "\n\n" + "Please answer me in " + language
        }])
        


@cl.on_message
async def run_conversation(user_message: object):
    if '/upload' == str(user_message):
        if not os.path.exists('./tmp'):
            os.mkdir('./tmp')
        files = await cl.AskFileMessage(
            content="Please upload a file.",
            max_size_mb=10,
            accept=[
                "*"
            ]).send()
        file = files[0]
        save_path = ""
        # 保存文件到paths目录下
        # 判断paths目录是否存在
        if save_path == "":
            save_path = file.name
        file_path = f"./tmp/{save_path}"
        # 保存文件
        content = file.content
        # 保存文件
        # content是bytes类型
        with open(file_path, "wb") as f:
            f.write(content)
        message_history = cl.user_session.get("message_history")
        message_history.append({
            "role": "assistant",
            "content": f"upload file ./tmp/{save_path} success"
        })
        language = config_env['openai']['language']
        await cl.Message(
            author="Chatbot",
            content=f"{get_text(language, 'upload_notification')} ./tmp/{save_path}",
        ).send()
        return
    
    await on_message(user_message)


@cl.on_stop
async def stop_chat():
    global is_stop
    print("stop chat")
    is_stop = True
