from sqlalchemy import create_engine
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

x = Pessoa(nome='Joao', usuario='joao', senha='1234')
y = Pessoa(nome='', usuario='joao', senha='1234')

session.add_all([x, y])
session.rollback()
session.commit()