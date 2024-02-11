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

x = Pessoa(nome='Liz', usuario='liz', senha='1657')
y = Pessoa(nome='Isaac', usuario='isaac', senha='6474')

session.add_all([x, y])
session.commit()