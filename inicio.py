import pymysql.cursors

con = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    db="aulapythonfull",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor)

def criar_tabela(nome_tabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"CREATE TABLE {nome_tabela} (Nome varchar(50))")
        print(f'Tabela "{nome_tabela}" criada com sucesso!')
    except Exception as e:
        print(f'Ocorreu um erro {e}')
    finally:
        con.close()

def remover_tabela(nome_tabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"DROP TABLE {nome_tabela}")
        print(f'Tabela "{nome_tabela}" excluída com sucesso!')
    except Exception as e:
        print(f'Ocorreu um erro {e}')
    finally:
        con.close()

def inserir_nome(nome):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO teste values ('{nome}')")
            print(f'O nome "{nome}" foi inserido com sucesso!')
    except Exception as e:
        print(f'Ocorreu um erro {e}')
    finally:
        con.close()

def mostrar_nomes():
    try:
        with con.cursor() as cursor:
            cursor.execute(f"SELECT * FROM teste")
            resultado = cursor.fetchall()
            for i in resultado:
                print(i['Nome'])
    except Exception as e:
        print(f'Ocorreu um erro {e}')
    finally:
        con.close()

def alterar_nome(nome_alterar, novo_nome):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"UPDATE teste SET Nome ='{novo_nome}' WHERE Nome = '{nome_alterar}' ")
            print('Nome alterado com sucesso')
    except Exception as e:
        print(f"Ocorreu um erro {e}")
    finally:
        con.close()

def excluir_nome(nome_excluir):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"DELETE from teste WHERE Nome = '{nome_excluir}'")
            print("Nome excluído com sucesso")
    except Exception as e:
        print(f"Ocorreu um erro {e}")
    finally:
        con.close()

