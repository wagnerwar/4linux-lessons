from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
   
engine = create_engine('sqlite:///banco.db')
Base = declarative_base()
 
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key = True, autoincrement = True)
    login = Column(String,  unique = True)
    senha = Column(String)
    nome = Column(String)

class Produto(Base):
    __tablename__ = "produto"
    id = Column(Integer, primary_key = True, autoincrement = True)
    id_usuario = Column(Integer, ForeignKey("usuario.id"))
    imagem = Column(String, unique = True, nullable = False)
    descricao = Column(String)
    data_cadastro = Column(DateTime, nullable = True, default=datetime.now())

""" 
if __name__ ==  '__main__':
    Base.metadata.create_all(engine)
"""
