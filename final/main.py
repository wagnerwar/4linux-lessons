from conexao import Usuario, session
from ClienteDAO import ClienteDAO
from ProdutoDAO import ProdutoDAO

logado = None

def deslogin():
    global logado
    logado = None
    menuLogin()

def menuOpcoes():
    global logado
    opt = None
    while(opt == None):
        print("1-Atualizar informacoes, 2-Excluir-se 3-Sair 4-Cadastrar produtos")
        opt = raw_input("Digite sua opcao: ")
                
        if(opt == "1"):
            usuario = session.query(Usuario).filter(Usuario.login == logado).first()
            if(usuario):
                print("Seus dados")
                print("\n Nome: {0}".format(usuario.nome))
                print("\n login: {0}".format(usuario.login))
                print("\n Senha: ****")
                senha = raw_input("Qual e a tua senha? ") or usuario.senha
                nome = raw_input("Qual e o teu nome? ") or usuario.nome
                usuario.nome = nome
                usuario.senha = senha
                session.commit()
                print("Usuario atualizado com sucesso")
                opt = None
            else:
               deslogin() 
        elif(opt == "2"):
            usuario = session.query(Usuario).filter(Usuario.login == logado).first()
            if(usuario):
                try:
                    session.delete(usuario)
                    session.commit()
                    print("Usuario excluido com sucesso")
                except Exception as e:
                    print(e)
                    print("Erro na delecao de usuario")
            opt = None
        elif(opt == "3"):
            print("Caiu aqui")
            deslogin()
            # opt = None
        elif(opt == "4"):
            usuario = session.query(Usuario).filter(Usuario.login == logado).first()
            if(usuario):
                print("Cadastro de produtos")
                imagem = raw_input("DIgite sua imagem")
                descricao = raw_input("DIgite a descricao da imagem")
                retorno = ProdutoDAO.cadastrar(usuario.id, imagem, descricao)
                if(retorno == True):
                   print("Inclusao de produto feiita com sucesso")
                else:
                   print("Erro na inclusao de produto. Tente novamente mais tarde")
                opt = None
            else:
                deslogin()
        else:
            opt = None

def menuLogin():
    global logado
    option = None
    while( logado == None ):
        print("SIstema de gerenciamento de maquinas DOCKER")
        print("1 - Cadastro 2-login 3-Sair")
        option = raw_input("Selecione a sua opcao: ")
        login, senha = None, None
        if(option == "1"):
            while(login == None or senha == None):
                login = raw_input("Digite seu login: ")
                senha = raw_input("DIgite sua senha: ")
            nome = raw_input("Digite seu nome: ")
            
            retorno = ClienteDAO.cadastrar(login, senha, nome) 
            if(retorno == True):
                print("Cadastro realizado com sucesso")
            else:
                print("Erro no cadastro")
        elif(option == "2"):
            while(login == None or senha == None):
                login = raw_input("DIgite seu login: ")
                senha = raw_input("Digite sua senha: ")
            usuario = session.query(Usuario).filter(Usuario.login == login, Usuario.senha == senha).first()
            if(usuario):
                logado = login
                print("Usuario logado com sucesso")
                menuOpcoes()
            else:
                print("Usuario nao autenticado")    
        elif(option == "3"):
            exit()

menuLogin()

