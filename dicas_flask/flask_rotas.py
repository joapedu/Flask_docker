from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template("index.html")

## Com o "@app.route" é possível mapear rotas para um html
## específico, apenas trocando o "/" por "/login" por exemplo.
