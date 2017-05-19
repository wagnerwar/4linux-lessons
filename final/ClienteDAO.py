from conexao import Usuario, session


class ClienteDAO(object):

    @staticmethod
    def cadastrar(login, senha, nome):
        if(session.query(Usuario).filter(Usuario.login == login).first()):
            print("Usuario ja existente")
            return False
        user = Usuario()
        user.login = login
        user.senha = senha
        user.nome = nome
        try:
            session.add(user)
            session.commit()
            return True
        except Exception as e:
            print(e)
            print("Erro no cadastro")
            return False
       
