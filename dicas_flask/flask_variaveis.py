from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    fruta1 = "Morango"
    fruta2 = "Uva"
    fruta3 = "Maçã"
    fruta4 = "Laranja"
    
    return render_template("index.html",
    fruta1=fruta1,
    fruta2=fruta2,
    fruta3=fruta3,
    fruta4=fruta4)

##Quando for anunciar a variável no html colocar assim {{exemplo}}


@app.route('/sobre')
def sobre():
    return render_template("sobre.html")
