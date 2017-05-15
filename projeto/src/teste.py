from paramiko.client import SSHClient
import paramiko
client = SSHClient()

# PARAMIKO e um plugin que permite estabelecer conexoes SSH via script em PYTHON

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect("127.0.0.1", username="root", password="4linux")

stdin, stdout, stderr = client.exec_command("ls -la")


print(stdout.read())



