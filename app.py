import flask
import sqlite3

app = flask.Flask(__name__)

@app.get("/")
def get_home():
    return flask.render_template("home.html")

@app.get('/produtos')
def get_produtos():
    sql_select_produtos = '''
    SELECT img, preco, nome FROM produtos ORDER BY preco DESC;
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


@app.get('/pesquisar')
def get_pesquisar():
    return flask.render_template("pesquisar.html")

@app.post("/pesquisar")
def post_pesquisar():
    preco = flask.request.form["preco"]
    nome = flask.request.form["nome"]
    
    sql_select_produtos_por_preco = f'''
    SELECT img, preco, nome FROM produtos WHERE preco <= '{preco}' ORDER BY preco DESC;
'''
    sql_select_produtos_por_nome = f'''
    SELECT img, preco, nome FROM produtos WHERE nome LIKE'%{nome}%' ORDER BY nome ASC;
'''

    with sqlite3.Connection('produtos.db') as conn:
        if preco:
            lista_de_produtos = conn.execute(sql_select_produtos_por_preco)
        elif nome:
            lista_de_produtos = conn.execute(sql_select_produtos_por_nome)
        else:
            lista_de_produtos = [('','0,00','não encontrado')]
    
    return flask.render_template("lista_produtos.html", produtos=lista_de_produtos)


app.run(host='0.0.0.0', debug=True)
