#!/usr/bin/env python

import paramiko
import re

host = '172.16.10.1'
sshport = 22
usr = 'fail2ban'
pkeyfile = '/home/dreyman_pa/.ssh/id_rsa'
blocklist_asterisk = '/home/dreyman_pa/BLOCKED_IP_ASTERISK'
blocklist_db       = '/home/dreyman_pa/BLOCKED_IP_DB'

# create file BLOCKED_IP_DB
def create_block_file(blklist_raw,blklist):
    infile = open(blklist_raw, 'r')
    outfile = open(blklist, 'w')

    for str in infile: 
#	print(str)
	pattern = re.compile(r"^REJECT\s+(\S+)\s+(\S+)\s+(\d+\.\d+\.\d+\.\d+)")
	for match in pattern.finditer(str):
	    #print(match.group(3))
	    outfile.write(match.group(3) + '\n')
    infile.close()
    outfile.close()

def pysshconnect(hostname, port, user, pkey_file, blklist):
    outfile = open(blklist, 'r')

    # ssh connect to Mikrotik
    if __name__ == "__main__":
	key = paramiko.RSAKey.from_private_key_file(pkey_file)
#	paramiko.util.log_to_file('paramiko.log')
	s = paramiko.SSHClient()
	s.load_system_host_keys()
	s.connect(hostname, port, username=user, pkey=key)

	for ipaddr in outfile:
#	    print ipaddr.strip()
	    cmd = "ip firewall address-list add address={0} timeout=604800 list=VoIP_Block"
	    cmdf = cmd.format(ipaddr.strip())
	    stdin, stdout, stderr = s.exec_command(cmdf)
	    print stdout.read()
	s.close()
    outfile.close()

def main():
    create_block_file(blklist_raw = blocklist_asterisk, blklist = blocklist_db)
    pysshconnect(hostname = host, port = sshport, user = usr, pkey_file = pkeyfile, blklist = blocklist_db)

if __name__ == "__main__":
    main()
