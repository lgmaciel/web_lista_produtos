import flask

app = flask.Flask(__name__)

lista_de_produtos = [
    (
        'https://www.freepnglogos.com/uploads/notebook-png/download-laptop-notebook-png-image-png-image-pngimg-2.png',
        '150,00',
        'Coisa 1'
    ),

    (
        'https://www.freepnglogos.com/uploads/notebook-png/download-laptop-notebook-png-image-png-image-pngimg-2.png',
        '250,00',
        'Coisa 2'
    ),

    (
        'https://www.freepnglogos.com/uploads/notebook-png/download-laptop-notebook-png-image-png-image-pngimg-2.png',
        '350,00',
        'Coisa 3'
    ),

    (
        'https://www.freepnglogos.com/uploads/notebook-png/download-laptop-notebook-png-image-png-image-pngimg-2.png',
        '450,00',
        'Coisa 4'
    )

]

@app.get('/')
def get_home():
   
    return flask.render_template("lista_produtos.html", produtos=lista_de_produtos)


app.run(host='0.0.0.0', debug=True)