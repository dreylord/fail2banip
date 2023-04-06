#!/usr/bin/env python

import paramiko

hostname = '172.16.10.1'
port = 22
username = 'fail2ban'
password = ''

if __name__ == "__main__":
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname,port,username,password)
    stdin, stdout, stderr = s.exec_command('user print')
    print stdout.read()
    s.close()
