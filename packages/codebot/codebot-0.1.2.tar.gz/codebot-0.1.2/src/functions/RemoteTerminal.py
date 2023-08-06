import asyncio
import paramiko

class RemoteTerminal:
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.hostname, username=self.username, password=self.password)
        self.timer = None

    def reset_timer(self):
        if self.timer:
            self.timer.cancel()
        self.timer = asyncio.get_event_loop().call_later(150, self.close)

    def run_cmd(self, cmd):
        if self.client is None:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(self.hostname, username=self.username, password=self.password)

        self.reset_timer()
        stdin, stdout, stderr = self.client.exec_command(cmd)
        return stdout.read().decode(), stderr.read().decode()

    def close(self):
        if self.client:
            self.client.close()
            self.client = None
