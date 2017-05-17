from pymongo import MongoClient
client = MongoClient('127.0.0.1')
db = client['devops']

# criacao de email


def incluiEmail():
    global db

    rem = raw_input("Digite o email do remetente")
    dest = raw_input("Digite o email do destinatario")
    ass = raw_input("DIgite o assunto da mensagem")
    msg = raw_input("Digite o corpo da mensagem")

    col = db.email
    col.insert({"remetente":rem,"destinatario":dest,"assunto":ass,"mensagem":msg})


def listarEmails():
    global db
    count = 1
    print("Listando fila de email")
    
    if db.email.count() == 0:
        print("Nenhum email encontrado")
        return

    for i in db.email.find():
        print("\nOrdem: {0}".format(count))
        print("Remetente: {0}".format(i['remetente']))
        print("Destinatario: {0}".format(i['destinatario']))
        print("Assunto: {0}".format(i['assunto']))
        print("Mensagem: {0}".format(i['mensagem']))
        count+=1
        

def disparaEmail():
    global db
    print("Disparando emails")
    if (db.email.count() == 0):
        print("Nenhum email encontrado")
        return

    for i in db.email.find():
        print("ENviando email de {0} para {1}".format(i['remetente'], i['destinatario']))
        db.email.remove({"_id":i['_id']})
        print("Email enviado")
    
# MAIN
rem, dest, ass, msg = None,None, None, None

option = None
while(option != "4"):
    
    print("Sistema de envio de emails")
    print("1-Cadastro 2-listagem  3-Disparar email 4-Sair")
    option = raw_input("Qual e a sua opcao: ")

    if(option == "1"):
        incluiEmail()
    elif(option == "2"):
        listarEmails()
    elif(option == "3"):
        disparaEmail()
    elif(option == "4"):
        exit()
