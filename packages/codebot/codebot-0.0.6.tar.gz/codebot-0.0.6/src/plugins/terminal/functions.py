import asyncio
import subprocess

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
        # Automatically execute the command and get the output of the entire terminal
        process = await asyncio.create_subprocess_shell(
            cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        if process.returncode != 0:
            # The command had a non-zero exit code, return the error message
            return {"output": stdout.decode(), "status": False, "error": stderr.decode(), "askUser": True, "cmd": cmd}
        else:
            return {"output": stdout.decode(), "status": True, "askUser": False}
    except Exception as e:
        # An unexpected error occurred, return the error message
        return {"output": None, "status": False, "error": str(e), "askUser": True, "cmd": cmd}
