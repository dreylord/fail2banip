import paramiko

def pysshconnect-rsa():
    hostname = '172.16.10.1'
    port = 22
    user = 'fail2ban'
    pkey_file = '/home/dreyman_pa/.ssh/id_rsa'

    if __name__ == "__main__":
	key = paramiko.RSAKey.from_private_key_file(pkey_file)
	paramiko.util.log_to_file('paramiko.log')
	s = paramiko.SSHClient()
	s.load_system_host_keys()
	s.connect(hostname, port,username=user, pkey=key)
	stdin, stdout, stderr = s.exec_command('user print')
	print stdout.read()
	s.close()

def main():
    pysshconnect-rsa()
if __name__ == "__main__":
    main()
