# SQLALCHEMY

# create_engine permite a criacao das tabelas com base no codigo python
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://admin:4linux@localhost:5432/blog')
Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# Criacao das tabelas
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, nullable=False, unique=True )
    nome = Column(String, nullable=False )
    senha = Column(String, nullable=False)
    postagem = relationship("Postagem", back_populates="usuario")
class Postagem(Base):
    __tablename__ = 'postagem'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False )
    conteudo = Column(String, nullable=False )
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    usuario = relationship("Usuario", back_populates="postagem")

    
if __name__ ==  '__main__':
    Base.metadata.create_all(engine)

