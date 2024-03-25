import sqlite3

# Conectar ao banco de dados (ou criar um novo banco de dados se ele não existir)
conn_1 = sqlite3.connect('../dados/banco_1.db')
conn_2 = sqlite3.connect('../dados/banco_2.db')

def cria_bd():

    # Criar uma tabela para armazenar os dados
    conn_1.cursor().execute('''
        CREATE TABLE IF NOT EXISTS contas (
            cpf TEXT,
            saldo DOUBLE
        )
    ''')

    conn_1.commit()

    # Criar uma tabela para armazenar os dados
    conn_2.cursor().execute('''
        CREATE TABLE IF NOT EXISTS contas (
            cpf TEXT,
            saldo DOUBLE
        )
    ''')
    conn_2.commit() 

# Função para inserir um novo dado no banco de dados
def gravar_dado(cpf, saldo, conn):
    conn.cursor().execute('''
        INSERT INTO contas (cpf, saldo)
        VALUES (?, ?)
    ''', (cpf, saldo))
    conn.commit()

# Função para recuperar todos os dados do banco de dados
def obter_dados(conn):
    dados = conn.cursor().execute('''
        SELECT * FROM contas
    ''')
    return dados.fetchall()

if __name__ == '__main__':
    cria_bd()
    gravar_dado('33333333333', 2000, conn=conn_1)
    gravar_dado('44444444444', 3000, conn=conn_2)
    print(obter_dados(conn_1))
    print(obter_dados(conn_2))