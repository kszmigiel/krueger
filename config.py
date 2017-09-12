import configparser
import threading
import paramiko
import os
import sys
import time

if len(sys.argv) < 2:
    print('Not enough parameters')
    exit(1)

f_path = sys.argv[1]
if not os.path.exists(sys.argv[1]):
    print('File {f_path} does not exist'.format(f_path=f_path))
    exit(2)

config = configparser.RawConfigParser()
fp = open(f_path)
config.readfp(fp)

sections = config.sections()
if 'commands' not in sections:
    print('You need to have a `commands` section in your config file')
    exit(3)

servers = list(sections)
servers.remove('commands')
commands = config.items('commands')

str_format = '{alias:<10} {command:<10} {output:>90}'
print(str_format.format(alias='Alias', command='Command', output='Output (stdout and stderr)'))
print(str_format.format(alias='-'*5, command='-'*7, output='-'*90))


def run_cmd(srv, hostname, username, password, cmd, cmd_id):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=hostname,
                   username=username,
                   password=password)
    stdin, stdout, stderr = client.exec_command(cmd)

    output = '{} {}'.format(stdout.read().strip().decode('utf-8'), stderr.read().strip().decode('utf-8'))

    sys.stdout.write(str_format.format(alias=srv,
                            command=cmd_id,
                            output=output)+"\n")
    return True


threads = []
thread_count = 0
for command in commands:
    cmd_id = command[0]
    cmd = command[1]

    for srv in servers:
        t = threading.Thread(target=run_cmd, kwargs={'srv': srv,
                                                              'hostname': config.get(srv, 'hostname'),
                                                              'username': config.get(srv, 'username'),
                                                              'password': config.get(srv, 'password'),
                                                              'cmd': cmd,
                                                              'cmd_id': cmd_id})
        t.start()
        threads.append(t)
        thread_count += 1

while True in [t.isAlive() for t in threads]:
    time.sleep(0.2)

print('Threads used: {thread_count}'.format(thread_count=thread_count))
