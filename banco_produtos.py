import sqlite3

conn = sqlite3.Connection('produtos.db')
sql_criar_tabela_produtos = '''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY,
	img TEXT NOT NULL,
	preco TEXT NOT NULL,
	nome TEXT NOT NULL
);
'''

conn.execute(sql_criar_tabela_produtos)
conn.commit()

sql_insert_produtos = '''
INSERT INTO PRODUTOS (img, preco, nome) VALUES (?, ?, ?);
'''

lista_de_produtos = [
    (
        '1.jpg',
        '150,00',
        'Coisa 1'
    ),

    (
        '2.png',
        '250,00',
        'Coisa 2'
    ),

    (
        '3.jpg',
        '150,00',
        'Coisa 3'
    ),

    (
        '4.jpg',
        '150,00',
        'Coisa 4'
    ),

    (
        '5.jpg',
        '150,00',
        'Coisa 5'
    ),

    (
        '6.jpg',
        '150,00',
        'Coisa 6'
    ),

    (
        '7.jpg',
        '150,00',
        'Coisa 7'
    ),

    (
        '8.jpg',
        '150,00',
        'Coisa 8'
    ),

]


conn.executemany(sql_insert_produtos, lista_de_produtos)
conn.commit()

conn.close()
