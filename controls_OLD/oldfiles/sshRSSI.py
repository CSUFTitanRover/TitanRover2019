import paramiko
server = "192.168.1.200"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

while True:
	ssh.connect(server, username="admin", password="titanrover17")
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("mca-status | grep signal")
	signal = ssh_stdout.readlines()[0]
	signal = int('-' + ''.join(i for i in signal if i.isdigit()))
	print(signal)
