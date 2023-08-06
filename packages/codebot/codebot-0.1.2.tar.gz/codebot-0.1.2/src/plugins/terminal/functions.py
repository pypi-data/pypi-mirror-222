import asyncio
import subprocess
from functions.RemoteTerminal import RemoteTerminal
import chainlit as cl
import uuid


remote_terminal_dict = {}

async def terminal(cmd: str, is_auto_run: bool = True):
    """
    if user ask about the Ubuntu question, you can use this function to answer it
    Parameters: 
        cmd: str(required) it must be a command that can be executed in the terminal, The command must be non-blocking and return results.If you encounter a situation where the sudo command is required, you need to automatically input the password in the cmd instead of waiting for terminal input. No command should generate any terminal input.
        is_auto_run: bool(optional) if it is True, the terminal will run the command automatically, otherwise, it will ask the user to run it, You need to decide whether to automatically execute the command based on whether it will have a certain impact.
    """
    if is_auto_run:
        return await run_cmd(cmd)
    else:
        return {"output": "Should we run the command: " + cmd + "?", "status": True, "askUser": True}

async def run_cmd(cmd: str):
    try:
        
        user_id = cl.user_session.get("user_id")
        if user_id is None:
            user_id = str(uuid.uuid4())
            cl.user_session.set("user_id", user_id)
        if user_id not in remote_terminal_dict:
            username = cl.user_session.get("username")
            password = cl.user_session.get("password")
            hostname = cl.user_session.get("hostname")
            if username is None:
                res = await cl.AskUserMessage("Please enter the username of the remote server: ").send()
                username = res["content"]
                cl.user_session.set("username", username)
            if password is None:
                res = await cl.AskUserMessage("Please enter the password of the remote server: ").send()
                password = res["content"]
                cl.user_session.set("password", password)
            if hostname is None:
                res = await cl.AskUserMessage("Please enter the hostname of the remote server: ").send()
                hostname = res["content"]
                cl.user_session.set("hostname", hostname)
            remote_terminal_dict[user_id] = RemoteTerminal(hostname, username, password)
        
        terminal = remote_terminal_dict[user_id]
        stdout, stderr = terminal.run_cmd(cmd)

        if stderr:
            # The command had a non-zero exit code, return the error message
            return {"output": stdout, "status": False, "error": stderr, "askUser": True, "cmd": cmd}
        else:
            return {"output": stdout, "status": True, "askUser": False}
    except Exception as e:
        # An unexpected error occurred, return the error message
        return {"output": None, "status": False, "error": str(e), "askUser": True, "cmd": cmd}

