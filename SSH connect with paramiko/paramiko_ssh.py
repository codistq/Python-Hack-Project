import paramiko


def sendCommand(command):
    stdin, stdout, error = ssh.exec_command(command)
    stdout_command = stdout.read()
    print(f"<<->{stdout_command.decode()}")


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host = "127.0.0.1"  # change here
port = 22  # change here (optional)
username = "anonymous"  # change here
password = "anonymous"  # change here

ssh.connect(host, port=port, username=username, password=password)
command = ""
while command.lower().split() != "":
    if command != "":
        sendCommand(command)
    command = input(">> ")
