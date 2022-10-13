from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    fruta = ["Morango", "Uva", "Laranja", "Mamão", "Maçã"]
    return render_template("index.html", fruta)

##  Quando for anunciar a lista no html colocar assim:
# {% for fruta in frutas%}
# <li> {{fruta}} </li> (li = listar)
# {% endfor %}

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")
