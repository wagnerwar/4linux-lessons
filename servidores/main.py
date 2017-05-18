#/usr/bin/python

from Classes import servidor, fisico, cloud
from pymongo import MongoClient

client = MongoClient('127.0.0.1')
db = client['devops']

con = db.servidores

option = None
print("### Sistema de manutencao de servidores ###")
while(option != "5"):
    print("1-Incluir servidor 2-Atualizar servidor 3-COnsultar servidor 4-Excluir servidor 5-Sair")

    option = raw_input("Digite a opcao desejada: ")

    if(option == "1"):
        nome = raw_input("Qual o nome de sua maquina? ")
        memoria = raw_input("Quanto tem de memoria? ")
        cpu = raw_input("Quanto tem de CPU? ")
        so = raw_input("Qual e o sistema operacional? ")

        tipo = raw_input("Qual e o tipo? 1-Fisico 2-Cloud")
        if(tipo == "1"):
            id_servidor = raw_input("Qual e o ID do servidor? ")
            localidade = raw_input("Qual e a localidade? ")
            machine = fisico()
            machine.definirAtributos(memoria, nome, cpu, so)
            machine.id_servidor = id_servidor
            machine.localidade = localidade
            try:
                # Validar o id
                con.insert({"nome": machine.getName(),"memoria": machine.getMemoria(),"cpu": machine.getCpu(),"so": machine.getSo(),"_id": machine.getId(),"localidade": machine.getLocalidade(), "tipo": "fisico" })
            except Exception as e:
                print(e)
                print("Erro na inclusao de maquina fisica")

        elif(tipo == "2"):
            UUID = raw_input("Qual e o ID do servidor? ")
            ambiente = raw_input("Qual e o ambiente? ")
            machine = cloud()
            machine.definirAtributos(memoria, nome, cpu, so)
            machine.UUID = UUID
            machine.ambiente = ambiente
            try:
                con.insert({"nome": machine.getName(),"memoria": machine.getMemoria(),"cpu": machine.getCpu(),"so": machine.getSo(),"_id": machine.getId(),"ambiente": machine.getAmbiente(), "tipo": "cloud" })
                print("Inclusao feita com sucesso!!")
            except Exception as e:
                print(e)
                print("Erro na inclusao de maquina fisica")

    elif(option == "2"):
       # atualizar
        ide = None
        while(ide == None):
            ide = raw_input("Qual e o ID do servidor? ")
        registros = con.find({"_id": ide})
        for i in registros:
            print(i)
            print("\n Consulta de servidores ")
            if(i['tipo'] == "fisico"):
                machine = fisico()
                machine.definirAtributos(i['memoria'],i['nome'],i['cpu'],i['so'])
                machine.id_servidor = i['_id']
                machine.localidade = i['localidade']
                nome = raw_input("Qual o nome de sua maquina? ") or machine.getName()
                memoria = raw_input("Quanto tem de memoria? ") or machine.getMemoria()
                cpu = raw_input("Quanto tem de CPU? ") or machine.getCpu()
                so = raw_input("Qual e o sistema operacional? ") or machine.getSo()
                localidade = raw_input("Digite a localizacao: ") or machine.getLocalidade()
                
                machine.nome = nome
                machine.memoria
                machine.cpu = cpu
                machine.so = so
                machine.localidade = localidade
                con.update({"_id": machine.id_servidor},{"nome": machine.getName(),"memoria": machine.getMemoria(),"cpu": machine.getCpu(),"so": machine.getSo(), "localidade": machine.getLocalidade()})
            elif(i['tipo'] == 'cloud'):
                machine = cloud()
                machine.definirAtributos(i['memoria'],i['nome'],i['cpu'],i['so'])
                machine.UUID = i['_id']
                machine.ambiente = i['ambiente']
                nome = raw_input("Qual o nome de sua maquina? ") or machine.getName()
                memoria = raw_input("Quanto tem de memoria? ") or machine.getMemoria()
                cpu = raw_input("Quanto tem de CPU? ") or machine.getCpu()
                so = raw_input("Qual e o sistema operacional? ") or machine.getSo()
                machine.nome = nome
                machine.memoria
                machine.cpu = cpu
                machine.so = so
                machine.ambiente = raw_input("DIgite o ambiente  ") or machine.ambiente  
                con.update({"_id": machine.UUID},{"nome": machine.getName(),"memoria": machine.getMemoria(),"cpu": machine.getCpu(),"so": machine.getSo(), "ambiente": machine.getAmbiente()})
    elif(option == "3"):
       # atualizar
        ide = None
        while(ide == None):
            ide = raw_input("Qual e o ID do servidor? ")
        registros = con.find({"_id": ide})
        for i in registros:
            print(i)
            print("\n Consulta de servidores ")
            if(i['tipo'] == "fisico"):
                machine = fisico()
                machine.definirAtributos(i['memoria'],i['nome'],i['cpu'],i['so'])
                machine.id_servidor = i['_id']
                machine.localidade = i['localidade']

                print("Nome: {0}".format(machine.getName()))
                print("Memoria: {0}".format(machine.getMemoria()))
                print("CPU: {0}".format(machine.getCpu()))
                print("Sistema operacional: {0}".format(machine.getSo()))
                print("ID do servidor: {0}".format(machine.getId()))
                print("Localidade: {0}".format(machine.getLocalidade()))

            elif(i['tipo'] == 'cloud'):
                machine = cloud()
                machine.definirAtributos(i['memoria'],i['nome'],i['cpu'],i['so'])
                machine.UUID = i['_id']
                machine.ambiente = i['ambiente']

                print("Nome: {0}".format(machine.getName()))
                print("Memoria: {0}".format(machine.getMemoria()))
                print("CPU: {0}".format(machine.getCpu()))
                print("Sistema operacional: {0}".format(machine.getSo()))
                print("UUID: {0}".format(machine.getId()))
                print("Ambiente: {0}".format(machine.getAmbiente()))
        
        else:
            print("Nenhum registro encontrado") 

    elif(option == "4"):
        pass
    elif(option == "5"):
        pass

