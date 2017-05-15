import conecta
from conecta import session, Produto


def menu():
    option = None
    while(option == None):
        print("SELECIONE UMA DAS OPCOES: ")
        print("1-Inclusao 2-Consulta 3-Atualizacao 4-Delecao 5-Listar os produtos 6-Sair")
        option = raw_input("Selecione: ")
    
    if(option == "1"):
        nome,descricao,quantidade = None, None, None
        while(nome == None):
            nome = raw_input("Informe um nome:")

        descricao = raw_input("Informe a descricao:")
        quantidade = raw_input("Informe a quantidade:")
        if(quantidade == None):
            quantidade = "0"
        qtd = int(quantidade)
        try:
            prod = Produto()
            prod.nome = nome
            prod.descricao = descricao
            prod.quantidade = qtd
            session.add(prod)
            session.commit()
        except Exception as e:
            print("Erro na inclusao")
        menu()
    elif (option == "2"):
        # COnsulta
        ide = raw_input("Informe o ID do produto")
        try:
            user = session.query(Produto).filter(Produto.id==int(ide)).first()
            if(user):
                print("INformacoes do produto: \n")
                print("ID: {0}".format(user.id))
                print("NOme: {0}".format(user.nome))
                print("Descricao: {0}".format(user.descricao))
                print("Quantidade: {0}".format(user.quantidade))
        except Exception as e:
            print(e)        
        menu() 
    elif (option == "3"):
        # Realizando uma atualizacao
        ide = raw_input("Informe o ID do produto")
        try:
            user = session.query(Produto).filter(Produto.id==int(ide)).first()
            if(user):
                user.nome = raw_input("Informe um nome:") or user.nome
                user.descricao = raw_input("Informe a descricao:") or user.descricao
                user.quantidade = int(raw_input("Informe a quantidade:") or user.quantidade)
                session.commit()
                print("Atualizacao feita com sucesso")
        except Exception as e:
            print(e)
        menu()
    elif (option == "4"):
        # Realizando uma delecao
        ide = raw_input("Informe o ID do produto")
        try:
            user = session.query(Produto).filter(Produto.id==int(ide)).first()
            if(user):
                session.delete(user)
                session.commit()
                print("Produto excluido")
        except Exception as e:
            print(e)
        menu()
    elif (option == "5"):
        try:
            produtos = session.query(Produto).all()
            for i in produtos:
                print("\n Id: {0}".format(i.id)) 
                print("Nome: {0}".format(i.nome))
                print("Descricao: {0}".format(i.descricao))
                print("Quantidade: {0}".format(i.quantidade))
        except Exception as e:
            print(e)
        menu()
    elif (option == "6"):
        print("BYE!!!")
    else:
        menu()
menu()


