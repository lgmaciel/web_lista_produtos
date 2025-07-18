import flask
import sqlite3

app = flask.Flask(__name__)

@app.get("/")
def get_home():
    return flask.render_template("home.html")

@app.get('/produtos')
def get_produtos():
    sql_select_produtos = '''
    SELECT img, preco, nome FROM produtos ORDER BY id DESC;
'''
    with sqlite3.Connection('produtos.db') as conn:
        lista_de_produtos = conn.execute(sql_select_produtos)
    
    return flask.render_template("lista_produtos.html", produtos=lista_de_produtos)


@app.get("/cadastrar")
def get_cadastrar():
    return flask.render_template("cadastro_produtos.html")


@app.post("/cadastrar")
def post_cadastrar():

    nome  = flask.request.form.get("nome")
    preco = flask.request.form.get("preco")
    img = flask.request.form.get("img")

    with sqlite3.Connection("produtos.db") as conn:
        sql_inserir_produto = '''
        INSERT INTO produtos (nome, preco, img) VALUES (?,?,?);
        ''' 
        conn.execute(sql_inserir_produto, (nome, preco, img))

    return flask.redirect("/produtos")

app.run(host='0.0.0.0', debug=True)
