import conexao
from conexao import session, Usuario, Postagem
from datetime import datetime, timedelta
from datetime import date


userlist = []

acesso = 0
tempo = 30

def autenticacao(autenticado=False):

    print("=" * 100) # Exibe = 100 vezes
    print("Autenticacao de usuario")
    autenticado = False
    while(autenticado == False):
        login = raw_input("Digite seu usuario: ")
        senha = raw_input("Digite sua senha")
        autenticado = False
        try:
            # autenticar
            valido = session.query(Usuario).filter(Usuario.login == login, Usuario.senha == senha).first()
            
            if(valido):
                autenticado = True
                geraToken() 
            else:
                print("NAO AUTENTICADO")
  
        except Exception as e:
            print("Erro na conexao")
            print(e)
"""
def buscarUsuario():
    usuario = raw_input("Informe o login do usuario")
    cons = con.cursor()
    cons.execute("select * from usuario WHERE login = '{0}'".format(usuario))
    if cons.fetchone():
        dado = cons.fetchone()
        print("Usuario encontrado")
        print("NOme: {0} ".format(dado["login"]))
        print("login: {0} ".format(dado["nome"]))
        print("Senha: {0}".format(dado["senha"]))
    else:
        print("Usuario nao encotrado")

def removerUsuario():
    usuario = raw_input("Informe o login do usuario")
    cons = con.cursor()
    try:
        cons.execute("delete from usuario WHERE login = '{0}'".format(usuario))
        con.commit()
    except Exception as e:
        con.rollback()
        print("Erro na delecao")
        return
    print("Delecao feita com sucesso")

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
    print("Usuario sera criado")
    cons = con.cursor()
    usuario, senha, nome, rsenha = None, None, None, None
    usuario = raw_input("Informe o usuario")
    senha = raw_input("Informe a senha")
    nome = raw_input("Informe o nome")
    rsenha = raw_input("Repita a senha")
    
    while(usuario == None):
        usuario = raw_input("Informe o login do usuario, lembrando que o mesmo nao pode ser preexistente")
    while(senha == None or senha != rsenha):
        senha = raw_input("Informe sua senha corretamente")
        rsenha = raw_input("Repita sua senha")
    try:
        cons.execute("INSERT INTO usuario VALUES('{0}','{1}','{2}')".format(usuario, nome, senha))
        con.commit()
    except Exception as e:
        print("Erro na inclusao")
        con.rollback()
        return   
    
    print("Usuario {0} ja cadastrado").format(nome)

def listarUsuario():
    print("Listar usuarios")
    for i in userlist:
        print("Usuario: {0} ".format(i["usuario"]))
        print("Senha: {0}".format(i["senha"]))
        print("Nome: {0}".format(i["name"]))
        print("\n")
        print("postagens")
        for p in i["postagem"]:
            print("\n")
            print("ID: {0}".format(p["id"]))  
            print("titulo: {0}".format(p["titulo"]))
            print("Conteudo: {0}".format(p["conteudo"]))

def criarPostagem(login):
    print("Criacao de postagem")
    cons_user = con.cursor()
    try:
        cons_user.execute("SELECT login from usuario WHERE login = '{0}'".format(login))
        if cons_user.fetchone():  
            titulo = raw_input("Digite o titulo: ")
            conteudo = raw_input("Digite o conteudo: ")
            ins_pos = con.cursor()
            ins_pos.execute("INSERT INTO postagem(id_usuario, titulo, conteudo) VALUES('{0}','{1}', '{2}') ".format(login, titulo, conteudo))
            con.commit()
            print("Postagem criada com sucesso")
            return
    except Exception as e:
        print(e)   
        return
    

def listaPostagens(login):
    cons_user = con.cursor()
    try:
        cons_user.execute("SELECT * FROM usuario WHERE login = '{0}' ".format(login))
        if cons_user.fetchone():
            cons_pos = con.cursor()
            cons_pos.execute("SELECT * FROM postagem WHERE id_usuario = '{0}'".format(login))
            count = 1
            
            for c in cons_pos.fetchall():   
                print("\n")
                print("Ordem: {0}".format(str(count)))
                print("Titulo: {0}".format(c[1]))
                print("Conteudo : {0}".format(c[2]))
                count+=1
                
    except Exception as ex:
        print(ex)
        return

def removerPostagem(login):
    cons_user = con.cursor()
    try:
        cons_user.execute("SELECT login from usuario WHERE login = '{0}'".format(login))
        if cons_user.fetchone():    
            ide = None
            while(ide == None):
                ide = raw_input("Digite o ID da postagem")
            cons_del = con.cursor()
            
            cons_del.execute("DELETE FROM postagem WHERE id = '{0}'".format(ide))            
            con.commit()    
            print("Exclusao feita com sucesso")
        else:
            print("Erro na exclusao")
            return
    except Exception as e:
        print("Erro na exclusao")
        return


def geraToken():
    global acesso
    acesso = datetime.now()
    return True

def checaToken():
    agora = datetime.now()
    global acesso
    global tempo
    if(agora - acesso).total_seconds() > tempo:
         
        print("TOKEN EXPIROU")
        return False    
    else:
        print(agora - acesso)
        print("TOKEN VALIDO")
        return True
"""
def removerPostagem(login):
    usuario = session.query(Usuario).filter(Usuario.login == login).first()
    try:
        if (usuario):    
            ide = None
            while(ide == None):
                ide = raw_input("Digite o ID da postagem")
            post = session.query(Postagem).filter(Postagem.id == ide).first()
            if(post):
                session.delete(post)
                session.commit()    
            print("Exclusao feita com sucesso")
        else:
            print("Usuario nao encontrado")
            return
    except Exception as e:
        print("Erro na exclusao")
        print(e)
        return

def buscarUsuario():
    usuario = raw_input("Informe o login do usuario")
    cons = con.cursor()
    cons.execute("select * from usuario WHERE login = '{0}'".format(usuario))
    if cons.fetchone():
        dado = cons.fetchone()
        print("Usuario encontrado")
        print("NOme: {0} ".format(dado["login"]))
        print("login: {0} ".format(dado["nome"]))
        print("Senha: {0}".format(dado["senha"]))
    else:
        print("Usuario nao encotrado")

def removerUsuario():
    login = raw_input("Informe o login do usuario")
    usuario = session.query(Usuario).filter(Usuario.login == login).first()
    if(usuario):
        try:
            session.delete(usuario)
            session.commit()
        except Exception as e:
            session.rollback()
            print("Erro na delecao")
            print(e)
            return
    print("Delecao feita com sucesso")

def criarUsuario():
    print("Usuario sera criado")
    usuario, senha, nome, rsenha = None, None, None, None
    usuario = raw_input("Informe o usuario")
    senha = raw_input("Informe a senha")
    nome = raw_input("Informe o nome")
    rsenha = raw_input("Repita a senha")
    
    while(usuario == None):
        usuario = raw_input("Informe o login do usuario, lembrando que o mesmo nao pode ser preexistente")
    while(senha == None or senha != rsenha):
        senha = raw_input("Informe sua senha corretamente")
        rsenha = raw_input("Repita sua senha")
    try:
        user = Usuario()
        user.login = usuario
        user.senha = senha
        user.nome = nome
        session.add(user)
        session.commit()
    except Exception as e:
        print("Erro na inclusao")
        session.rollback()
        return   
    
    print("Usuario {0} ja cadastrado").format(nome)
def listaPostagens(login):
    try:
        usuario = session.query(Usuario).filter(Usuario.login == login).first()
        if usuario:
            posts = usuario.postagem
            
            count = 1
            
            for c in posts:   
                print("\n")
                print("Ordem: {0}".format(str(count)))
                print("Titulo: {0}".format(c.titulo))
                print("Conteudo : {0}".format(c.conteudo))
                count+=1
                
    except Exception as ex:
        print(ex)
        return

def criarPostagem(login):
    print("Criacao de postagem")
    try:
        usuario = session.query(Usuario).filter(Usuario.login == login).first()
       
        if usuario:  
            titulo = raw_input("Digite o titulo: ")
            conteudo = raw_input("Digite o conteudo: ")
            post = Postagem()
            post.titulo = titulo
            post.conteudo = conteudo
            usuario.postagem.append(post)
            session.add(post)
            session.commit()
            print("Postagem criada com sucesso")
            return
    except Exception as e:
        print(e)   
        return

def menu():
    option = None
    while option != "6":
        print("=" * 50)
        print("SIstema de administracao de imagens do Docker")
        print("=" * 50)
        print("1) Criar novo usuario")
        print("2) Listar usuario e suas postagens")
        print("3) Remover usuario")
        print("4) Criar postagem")
        print("5) Remover postagem")
        print("6) Sair")
    
        option = raw_input("INforme sua opcao")
    
        if(option == "1"):
            criarUsuario()
        elif(option == "2"):
            if(checaToken() == False):
                autenticacao(False)
                
            login = None
            while(login == None):
                login = raw_input("DIgite o login: ")
            listaPostagens(login)

        elif(option == "3"):
            removerUsuario()
        elif(option == "4"):
            login = None
            while(login == None):
                login = raw_input("DIgite o login: ")
            criarPostagem(login)
        elif(option == "5"):
            login = None
            while(login == None):
                login = raw_input("DIgite o login: ")
            removerPostagem(login)
    
        elif(option == "6"):
            print("XAU!!")
            exit()

def geraToken():
    global acesso
    acesso = datetime.now()
    return True

def checaToken():
    agora = datetime.now()
    global acesso
    global tempo
    if(agora - acesso).total_seconds() > tempo:
         
        print("TOKEN EXPIROU")
        return False    
    else:
        print(agora - acesso)
        print("TOKEN VALIDO")
        return True
# main
autenticado = False

autenticacao(autenticado)

menu()
 
