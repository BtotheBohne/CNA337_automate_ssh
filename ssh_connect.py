#pkey source: https://gist.github.com/batok/2352501
#stdout source: https://stackoverflow.com/questions/8138241/after-executing-a-command-by-python-paramiko-how-could-i-save-result
import paramiko

#set variables
ssh = paramiko.SSHClient()
host = "ec2-3-21-231-7.us-east-2.compute.amazonaws.com"
user = "ubuntu"
k = paramiko.RSAKey.from_private_key_file(r"C:\Users\bdboh\Documents\ben_ubuntu_key.pem")

#connect to ec2
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="3.21.231.7", username=user, pkey=k)

#enter command
stdin, stdout, stderr = ssh.exec_command("sudo apt update && sudo apt upgrade -y")
stdin.flush()

data = stdout.readlines()
output = []

for line in data:
    output.append(line.strip("\n"))

for line in output:
    print(line)

ssh.close()
print("Done")