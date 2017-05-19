from conexao import Produto, session

class ProdutoDAO(object):

    @staticmethod
    def cadastrar(id_usuario, imagem, descricao):
        prod = Produto()
        prod.imagem = imagem
        prod.descricao = descricao
        if(session.query(Produto).filter(Produto.imagem == prod.imagem).first()):
            print("Imagem ja existe")
            return False
        prod.id_usuario = id_usuario
        try:
            session.add(prod)
            session.commit()
            return True
        except Exception as e:
            print(e)
            print("Erro na inclusao de produto")
            return False
