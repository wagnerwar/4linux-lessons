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

    id = Column(Integer, primary_key=True)
    nome = Column(String)

# Criacao das tabelas no banco de dados
if __name__ ==  '__main__':
    Base.metadata.create_all(engine)


# Estabelecendo conexao
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
# MAIN
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


