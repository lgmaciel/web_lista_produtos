import sqlite3

conn = sqlite3.Connection('produtos.db')

sql_criar_tabela_categoria_produto = '''
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);
'''

sql_criar_tabela_produtos = '''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY,
	img TEXT NOT NULL,
	preco TEXT NOT NULL,
	nome TEXT NOT NULL,
    id_categoria INTEGER NOT NULL,
    FOREIGN KEY(id_categoria) REFERENCES categorias(id)
);
'''
conn.execute(sql_criar_tabela_categoria_produto)
conn.execute(sql_criar_tabela_produtos)
conn.commit()

sql_insert_categorias = '''
INSERT INTO categorias (nome) VALUES (?)
'''
lista_de_categorias = [
    ('papelaria',),
    ('vestuario',),
    ('outros',)
]

conn.executemany(sql_insert_categorias, lista_de_categorias)


sql_insert_produtos = '''
INSERT INTO produtos (img, preco, nome, id_categoria) VALUES (?, ?, ?, ?);
'''
lista_de_produtos = [
    (
        '1.jpg',
        '150,00',
        'Coisa 1',
        '3'
    ),

    (
        '2.png',
        '250,00',
        'Coisa 2',
        '2'
    ),

    (
        '3.jpg',
        '150,00',
        'Coisa 3',
        '2'
    ),

    (
        '4.jpg',
        '150,00',
        'Coisa 4',
        '1'
    ),

    (
        '5.jpg',
        '150,00',
        'Coisa 5',
        '1'

    ),

    (
        '6.jpg',
        '150,00',
        'Coisa 6',
        '3'
    ),

    (
        '7.jpg',
        '150,00',
        'Coisa 7',
        '3'
    ),

    (
        '8.jpg',
        '150,00',
        'Coisa 8',
        '1'
    ),

]


conn.executemany(sql_insert_produtos, lista_de_produtos)
conn.commit()

conn.close()
