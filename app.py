import flask
import sqlite3

app = flask.Flask(__name__)

@app.get('/')
def get_home():
    sql_select_produtos = '''
    SELECT img, preco, nome FROM produtos;
'''
    with sqlite3.Connection('produtos.db') as conn:
        lista_de_produtos = conn.execute(sql_select_produtos)
    
    return flask.render_template("lista_produtos.html", produtos=lista_de_produtos)


app.run(host='0.0.0.0', debug=True)
