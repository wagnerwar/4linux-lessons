# SQLALCHEMY

# create_engine permite a criacao das tabelas com base no codigo python
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///banco.db')
Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# Criacao das tabelas
class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False, unique=True )
    descricao = Column(String)
    quantidade = Column(Integer)

"""
if __name__ ==  '__main__':
    Base.metadata.create_all(engine)
"""

