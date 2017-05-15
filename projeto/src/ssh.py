from paramiko.client import SSHClient
import paramiko
client = SSHClient()

diretorio = raw_input("Informe o diretorio a ser compactado")
nome_arquivo = raw_input("Informe o nome do arquivo de backup")

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect("127.0.0.1", username="root", password="4linux")

stdin, stdout, stderr = client.exec_command("tar -cvzf /backup/{1}.tar.gz {0}".format(diretorio, nome_arquivo))

print(stderr.read())
print(stdout.read())
