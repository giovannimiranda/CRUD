import sqlite3

dbase = sqlite3.connect('vendas.db')
cursor = dbase.cursor()
dbase.execute('''  CREATE TABLE IF NOT EXISTS vendas (
        marca TEXT NOT NULL,
        modelo TEXT,
        versao TEXT,
        ano INTEGER,
        preco INTEGER)'''
        )

dbase.commit()

def write(marca, modelo, versao, ano, preco):
    cursor.execute(''' INSERT into vendas(marca, modelo, versao, ano, preco) VALUES(?, ?, ?, ?, ?)''', (marca, modelo, versao, ano, preco))
    dbase.commit()

def read_task():
    cursor = dbase.cursor()
    cursor.execute(''' SELECT modelo from vendas''')
    data = cursor.fetchall()
    dbase.commit()
    return data
