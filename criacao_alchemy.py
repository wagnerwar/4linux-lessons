# SQLALCHEMY

# create_engine permite a criacao das tabelas com base no codigo python
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///banco.db')

"""
Deve-se ter instaladas as seguintes dependencia:
pycopg2
mysqlDB
"""

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Criacao da tabela 'usuarios'
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False, unique=True )

"""
# Criacao das tabelas no banco de dados
if __name__ ==  '__main__':
    Base.metadata.create_all(engine)
"""


# Estabelecendo conexao
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# MAIN
"""
try:
    # Realizando uma insercao
    session.add(Usuario(id=1, nome='Wagner NULL'))
    session.commit()

    # Caso a insercao seja condicao para outras insercoes 
    # session.flush()
    print('Insercao realizada com sucesso')
except Exception as e:
    print('Erro na inclusao')
    session.rollback()
"""

# Realizando uma consulta
"""
try:
    users = session.query(Usuario).all()
    for i in users:
        # Para realizar UPDATE, basta alterar qualquer propridade e executar o metodo commit()
        #i.nome = 'TESTE'
        #session.commit()
        print(i.nome)
    print(users)
except Exception as e:
    print("Erro na consulta")
"""

# nova forma de realizar insercao, tratando registros como objetos
"""
try:
    usuario = Usuario()
    usuario.nome = 'DFFFF'
    session.add(usuario)
    session.commit()
    
except Exception as e:
    print('Erro na insercao')
"""
# Realizando uma consulta de um valor
try:
    usuario = session.query(Usuario).filter(Usuario.id==2).first()
    print(usuario.nome)
    
except Exception as e:
    print("Erro na busca")
    print(e)


# Realizando uma delecao
"""
try:
    usuario = session.query(Usuario).filter(Usuario.id==2).first()
    session.delete(usuario)
    session.commit()
except Exception as e:
    print("Erro na delecao")
    print(e)
"""
