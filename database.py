import sqlite3

dbase = sqlite3.connect('clientes.db')
cursor = dbase.cursor()
dbase.execute('''  CREATE TABLE IF NOT EXISTS clientes (
        nome VARCHAR(50) NOT NULL,
        idade INTEGER,
        telefone TEXT,
        email TEXT NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        endereco TEXT,
        cidade TEXT,
        uf VARCHAR(2) NOT NULL)'''
        )

dbase.commit()

def write(nome, idade, telefone, email, cpf, endereco, cidade, uf):
    cursor.execute(''' INSERT into clientes(nome, idade, telefone, email, cpf, endereco, cidade, uf) VALUES(?, ?, ?, ?, ?, ?, ?, ?)''', (nome, idade, telefone, email, cpf, endereco, cidade, uf))
    dbase.commit()

def delete(x):
    cursor.execute(''' delete from clientes where nome=?''', x)
    dbase.commit()

def read_task():
    cursor = dbase.cursor()
    cursor.execute(''' SELECT nome from clientes''')
    data = cursor.fetchall()
    dbase.commit()
    return data