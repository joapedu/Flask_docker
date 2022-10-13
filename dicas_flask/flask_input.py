from flask import Flask, render_template, request ##para usar input
app = Flask(__name__)

lista = [] #declarar fora da função, se não cria repetidamente uma nova

@app.route('/', methods=["GET", "POST"]) #importante adcionar como lista
def principal():
    if request.method == "POST": #se tiver POST no html
        if request.form.get("lista"): # se o nome definido no html for preenchido
            lista.append(request.get("lista")) #request.get("lista") = input
    return render_template("index.html", lista=lista)
