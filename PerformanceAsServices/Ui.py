from flask import Flask, render_template, request,json
import sys
import os
import paramiko
from cryptography.hazmat.primitives.serialization import *
path = "C:\\Users\\Sanisetty.Vardhan\\PycharmProjects\\PerformanceAsAService"
app = Flask(__name__)
subfolder = os.listdir(path)
xml_jmx = []
for file in subfolder:
    if ".xml" in file or ".jmx" in file:
        xml_jmx.append(file)
print(xml_jmx)
@app.route('/')
def formpage():
    return render_template("index.html",xml_jmx= json.dumps(xml_jmx))

# @app.route('/Connect',methods=["Post"])
# def connectTovm():
#     Ip= request.form["virtual-ip"]
#     Uname= request.form["Username"]
#     Pwd= request.form["Password"]
#     return Uname

@app.route('/Connect',methods=["Post","Get"])
def ssh_command():
    ip= request.form["virtual-ip"]
    username= request.form["Username"]
    password= request.form["Password"]
    port=request.form["port"]
    paramiko.util.log_to_file("filename.log")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port, username, password)
    return formpage()

    # stdin, stdout, stderr = client.exec_command(command)
    # transport = ssh.get_transport()
    # session = transport.open_session()
    # session.set_combine_stderr(True)
    # session.get_pty()

    # bash_script = open("./script.sh").read()
    # # execute the BASH script
    # stdin, stdout, stderr = client.exec_command(bash_script)
    #
    # # input = stdin.read()
    # output = stdout.read()
    # # output_error = stderr.read()
    # print(output.decode('utf-8'))
    # # Close the connect
    # client.close()





if __name__ == "__main__":
    app.run(debug=True)