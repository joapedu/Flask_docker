# extrair do dicionário
notas = {"Fulano": 5.0, "Beltrano":6.0, "Aluno": 7.0, "Sicrano": 8.5}
for chave, valor in notas.items():
    print(chave)
    print(valor)

#aplicando flask com o extrair
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    notas = {"Fulano": 5.0, "Beltrano":6.0, "Aluno": 7.0, "Sicrano": 8.5}
    return render_template("index.html", notas)

##  Quando for anunciar odicionário no html colocar assim:
# {% for chave, valor in notas.items() %}
#   <details> (encapsular)
#       <summary> (apresentar)   
#           {{chave}}
#           <p> {{valor}} </p> (esconder)
#       </summary>
#   </details>
## {% endfor %}
