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

# x = session.query(Pessoa).all() # pegando tudo que está no banco de dados (retorna uma lista de objetos)
# for i in x:
#     print(f'ID: {i.id}')
#     print(f'NOME: {i.nome}')
#     print(f'SENHA: {i.senha}')
#     print('-' * 20)

# x = session.query(Pessoa).filter(Pessoa.nome == "Guilherme").all() # filtrando por uma única condição

# x = session.query(Pessoa).filter(Pessoa.nome == 'Guilherme').filter(Pessoa.usuario == 'guimont').all() # filtrando com mais de uma condição (operador and)
# x = session.query(Pessoa).filter_by(nome='Guilherme', usuario='guimont') # forma simplificada do 'and', utilizando o nome da coluna da tabela

x = session.query(Pessoa).filter(or_(Pessoa.nome == 'Guilherme', Pessoa.usuario == 'liz')) # utilizando o operador 'or' (importar o or_)

for i in x:
    print(f'ID: {i.id}')
    print(f'NOME: {i.nome}')
    print(f'USUARIO: {i.usuario}')
    print(f'SENHA: {i.senha}')
    print('-' * 20)