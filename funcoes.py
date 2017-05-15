# !/usr/bin/python

# ADMIN-SSH (Sera desenvolvido ao longo do curso)

def autenticacao(autenticado=False):

    print("=" * 100) # Exibe = 100 vezes
    print("Autenticacao de usuario")
    autenticado = False
    while(autenticado == False):
        login = raw_input("Digite seu usuario: ")
        senha = raw_input("Digite sua senha")
        autenticado = False
        for i in userlist:    
            if(i["usuario"] == login and i["senha"] == senha):
                print("Usuario autenticado")
                autenticado = True
                break


userlist = [{"usuario" : "admin", 
             "senha": "amesma", 
             "name": "Administrador", }]

autenticado = False

autenticacao(autenticado)


def buscarUsuario():
    usuario = raw_input("Informe o login do usuario")
    for i in userlist:
        if(i["usuario"] == usuario):
            print("Usuario encontrado")
            print("NOme: {0} ".format(i["usuario"]))
            print("login: {0} ".format(i["name"]))
            print("Senha: {0}".format(i["senha"]))
            break
        else:
            print("Usuario nao encotrado")

def removerUsuario():
    usuario = raw_input("Informe o login do usuario")
    for i in userlist:
        if(i["usuario"] == usuario):
            userlist.remove(i)
            print("usuario removido {0}".format(usuario))
            break
        else:
            print("Usuario nao encontrado")

def atualizarUsuario():
    usuario = raw_input("Informe o login do usuario")
    for i in userlist:
        if(i["usuario"] == usuario):
            i["name"] = raw_input("INforme o nome do usuario: ") or i["name"]
                
            usernew = raw_input("Informe o novo login") or i["usuario"]
            if(usernew != i["usuario"]):
                while(usernew == None) or \
                any(x["usuario"] == usernew for x in userlist):
                    usernew = raw_input("Login nao pode ser pre-existente")
                    i["usuario"] = usernew
                rsenha = None
                senha = None
                while(senha == None or rsenha == None or senha != rsenha):
                    senha = raw_input("Informe sua senha corretamente") or i["senha"]
                    rsenha = raw_input("Repita sua senha") or i["senha"]
                i["senha"] = senha

                print("USuario atualizado: {0} ".format(i["usuario"]))
                print(i)

def criarUsuario():
    print("Usuario criado")
    usuario, senha, nome, rsenha = None, None, None, None
    usuario = raw_input("Informe o usuario")
    senha = raw_input("Informe a senha")
    nome = raw_input("Informe o nome")
    rsenha = raw_input("Repita a senha")
        
    while(usuario == None) or \
        any(i["usuario"] == usuario for i in userlist):
        usuario = raw_input("Inform o login do usuario, lembrando que o mesmo nao pode ser preexistente")
    while(senha == None or senha != rsenha):
        senha = raw_input("Informe sua senha corretamente")
        rsenha = raw_input("Repita sua senha")
    userlist.append({"usuario": usuario,
                        "senha": senha,
                        "name": nome})
    print("Usuario {0} ja cadastrado").format(nome)

def listarUsuario():
    print("Listar usuarios")
    for i in userlist:
        print("Usuario: {0} ".format(i["usuario"]))
        print("Senha: {0}".format(i["senha"]))
        print("Nome: {0}".format(i["name"]))
        print("\n")

option = None
while option != "6":
    print("=" * 50)
    print("SIstema de administracao de imagens do Docker")
    print("=" * 50)
    print("1) Criar novo usuario")
    print("2) Buscar usuario")
    print("3) Remover usuario")
    print("4) atualizar usuario")
    print("5) listar todos os usuarios")
    print("6) Sair")

    option = raw_input("INforme sua opcao")
    
    if(option == "1"):
        criarUsuario()
    elif(option == "2"):
        buscarUsuario()
    elif(option == "3"):
        removerUsuario()
    elif(option == "4"):
        atualizarUsuario()
    elif(option == "5"):
        listarUsuario()
    elif(option == "6"):
        print("XAU!!")
"""
if all((i["usuario"] != login) for i in userList):
    print("Usuario incorreto")
else:
    print("Usuario autenticado com sucesso")

if all((i["senha"] != senha) for i in userList):
    print("Senha incorreta")
else:
    print("senha correta")
"""
exit()


