import sqlite3

dbase = sqlite3.connect('motocicleta.db')
cursor = dbase.cursor()
dbase.execute('''  CREATE TABLE IF NOT EXISTS motocicleta (
        marca TEXT NOT NULL,
        modelo TEXT,
        versao TEXT,
        ano INTEGER,
        preco INTEGER)'''
        )

dbase.commit()

def write(marca, modelo, versao, ano, preco):
    cursor.execute(''' INSERT into motocicleta(marca, modelo, versao, ano, preco) VALUES(?, ?, ?, ?, ?)''', (marca, modelo, versao, ano, preco))
    dbase.commit()

def delete(x):
    cursor.execute(''' delete from motocicleta where modelo=?''', x)
    dbase.commit()

def read_task():
    cursor = dbase.cursor()
    cursor.execute(''' SELECT modelo from motocicleta''')
    data = cursor.fetchall()
    dbase.commit()
    return data
