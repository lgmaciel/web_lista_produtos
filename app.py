import flask
import sqlite3
from secrets import token_hex

app = flask.Flask(__name__)
# Token usado para gerar o valor do cookie de sessão para um usuário
app.secret_key = token_hex()

@app.get("/")
def get_home():
    return flask.render_template("home.html")


@app.get("/login")
def get_login():
    return flask.render_template("login.html")

@app.post("/login")
def post_login():
    # Aqui vamos validar o login e criar a session do usuário
    
    # 1. recebemos os valores de login e senha do form de login
    login = flask.request.form['login']
    senha = flask.request.form['senha']
    
    # 2. consultar o banco para verificar se login e senha existem para o usuário
    sql_validar_login = f'''
    SELECT login, senha, nome, email
    FROM usuarios
    WHERE 
        login="{login}" AND senha="{senha}";
'''
    print(sql_validar_login)
    with sqlite3.Connection('produtos.db') as conn:
        dados_usuario = conn.execute(sql_validar_login)
        
        # Resposta no formato: [(login, senha, nome, email),]

        # se válido:
        # 3. criar a sessão do usuário
        try:
            # se dados_usuário contiver uma tupla com login, senha, nome, email
            login, _, nome, email = next(dados_usuario)
            # usuário válido (temos dados dele)
            # então criamos a sessão dele
            flask.session["login"] = login
            flask.session["nome"] = nome
            flask.session["email"] = email        
        except StopIteration:
            # Login inválido (dados_usuario estava vazio)
            return flask.redirect("/")
        
    return flask.redirect("/")

@app.get("/logout")
def get_logout():
    flask.session.clear()
    return flask.redirect('/')

@app.get('/produtos')
def get_produtos():
    sql_select_produtos = '''
    SELECT img, preco, nome, id FROM produtos ORDER BY preco DESC;
'''
    with sqlite3.Connection('produtos.db') as conn:
        lista_de_produtos = conn.execute(sql_select_produtos)
    
    return flask.render_template("lista_produtos.html", produtos=lista_de_produtos)

@app.get("/categoria/<id>")
def get_categoria(id):
    sql_select_produtos = f'''
    SELECT img, preco, nome, id FROM produtos 
    WHERE produtos.id_categoria = {id}
    ORDER BY nome;
'''
    with sqlite3.Connection('produtos.db') as conn:
        lista_de_produtos = conn.execute(sql_select_produtos)
    
    return flask.render_template("lista_produtos.html", produtos=lista_de_produtos)


@app.get("/cadastrar")
def get_cadastrar():
    with sqlite3.Connection('produtos.db') as conn:
        sql_select_categorias = "SELECT id, nome FROM categorias;"
        
        lista_categorias = conn.execute(sql_select_categorias)
        #retorno: [(1,'Papelaria'), (2, 'Vestuário'), (3, 'Outros')] 

    return flask.render_template("cadastro_produtos.html", categorias = lista_categorias)


@app.post("/cadastrar")
def post_cadastrar():

    nome  = flask.request.form.get("nome")
    preco = flask.request.form.get("preco")
    img = flask.request.form.get("img")
    categoria = flask.request.form.get("categoria")

    with sqlite3.Connection("produtos.db") as conn:
        sql_inserir_produto = '''
        INSERT INTO produtos (nome, preco, img, id_categoria) VALUES (?,?,?,?);
        ''' 
        conn.execute(sql_inserir_produto, (nome, preco, img, categoria))

    return flask.redirect(f"/categoria/{categoria}")


@app.get('/pesquisar')
def get_pesquisar():
    return flask.render_template("pesquisar.html")

@app.post("/pesquisar")
def post_pesquisar():
    preco = flask.request.form["preco"]
    nome = flask.request.form["nome"]
    
    sql_select_produtos_por_preco = f'''
    SELECT img, preco, nome, id FROM produtos WHERE preco <= '{preco}' ORDER BY preco DESC;
'''
    sql_select_produtos_por_nome = f'''
    SELECT img, preco, nome, id FROM produtos WHERE nome LIKE'%{nome}%' ORDER BY nome ASC;
'''

    with sqlite3.Connection('produtos.db') as conn:
        if preco:
            lista_de_produtos = conn.execute(sql_select_produtos_por_preco)
        elif nome:
            lista_de_produtos = conn.execute(sql_select_produtos_por_nome)
        else:
            lista_de_produtos = [('','0,00','não encontrado')]
    
    return flask.render_template("lista_produtos.html", produtos=lista_de_produtos)

@app.get("/excluir/<id_produto>")
def excluir_produto(id_produto):
    sql_excluir_produto = f'''
    DELETE FROM produtos WHERE id = {id_produto}
'''
    with sqlite3.Connection('produtos.db') as conn:        
        conn.execute(sql_excluir_produto)
        conn.commit()

    return flask.redirect("/")

app.run(host='0.0.0.0', debug=True)
