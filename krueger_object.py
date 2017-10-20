import configparser
import threading
import paramiko
import os
import sys
import time

class Krueger:

    def __init__(self, f_path, rsa_key):
        if not os.path.exists(f_path):
            raise ValueError('File {f_path} does not exist'.format(f_path=f_path))

        if not os.path.exists(rsa_key):
            raise ValueError('File {rsa_key} does not exist'.format(rsa_key=rsa_key))

        self.rsa_key = rsa_key

        self.config = configparser.RawConfigParser()
        self.config.readfp(open(f_path))

        self.sections = config.sections()
        if 'commands' not in self.sections:
            raise ValueError('You need to have a `commands` section in your config file')

        self.servers = list(sections)
        self.servers.remove('commands')
        self.commands = self.config.items('commands')

    def run_cmd(self, srv, hostname, username, cmd, cmd_id):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=hostname,
                       username=username,
                       key_filename=self.rsa_key)
        client.exec_command(cmd)

        return 0

    def run(self):
        for command in self.commands:
            cmd_id = command[0]
            cmd = command[1]

            for srv in self.servers:
                t = threading.Thread(target=self.run_cmd, kwargs={'srv': srv,
                                                             'hostname': self.config.get(srv, 'hostname'),
                                                             'username': self.config.get(srv, 'username'),
                                                             'cmd': cmd,
                                                             'cmd_id': cmd_id})
                t.start()
                threads.append(t)

        while True in [t.isAlive() for t in threads]:
            time.sleep(0.2)
