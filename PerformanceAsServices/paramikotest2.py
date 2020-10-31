import os
import paramiko

# def ssh_command(ip, port, username, password, command='pwd; ls'):
from cryptography.hazmat.primitives.serialization import ssh


def ssh_command(ip, port, username, password):
    paramiko.util.log_to_file("filename.log")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port, username, password)
    # stdin, stdout, stderr = client.exec_command(command)
    # transport = ssh.get_transport()
    # session = transport.open_session()
    # session.set_combine_stderr(True)
    # session.get_pty()

    bash_script = open("./script.sh").read()
    # execute the BASH script
    stdin, stdout, stderr = client.exec_command(bash_script)

    # input = stdin.read()
    output = stdout.read()
    # output_error = stderr.read()
    print(output.decode('utf-8'))
    # Close the connect
    client.close()


ssh_command('52.255.171.126', 22, 'AzureUser', 'P@ssW0rd123456')
