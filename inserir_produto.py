import sqlite3
import sys

match sys.argv[1:]:

    case ['inserir',nome, preco, img]:
        with sqlite3.Connection("produtos.db") as conn:
            sql_inserir_produto = '''
            INSERT INTO produtos (nome, preco, img) VALUES (?,?,?);
            ''' 
            conn.execute(sql_inserir_produto, (nome, preco, img))
            print('inserido.')

