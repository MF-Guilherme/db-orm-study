from sqlalchemy import create_engine, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from orm import Pessoa


def retorna_session():
    USUARIO = 'root'
    SENHA = ''
    HOST = 'localhost'
    BANCO = 'aulapythonfull'
    PORT = '3306'

    CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

session = retorna_session()


# x = session.query(Pessoa).filter(Pessoa.id == '7').delete() # Deletando o objeto diretamente
x = session.query(Pessoa).filter(Pessoa.id == '4').one() # outra opção, filtrando um objeto do banco
session.delete(x) # e deletando o objeto através da session

session.commit()