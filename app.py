import flask

app = flask.Flask(__name__)

@app.get('/')
def get_home():
    img = 'https://www.freepnglogos.com/uploads/notebook-png/download-laptop-notebook-png-image-png-image-pngimg-2.png'
    preco = '150,00'
    nome = 'Coisa'

    return flask.render_template("lista_produtos.html",
                                img_produto = img,
                                preco_produto = preco,
                                nome_produto = nome)


app.run(host='0.0.0.0', debug=True)