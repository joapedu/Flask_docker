import urllib.request, json

url_pop = "https://api.themoviedb.org/3//discover/movie?sort_by=popularity.desc&api_key=96275fcac06ba8cbe9d9d4e246f32038"
resposta_pop = urllib.request.urlopen(url_pop)      ##urlopen
dados_pop = resposta_pop.read()                     ##variável para read
jsondata_pop = json.loads(dados_pop)                ##transformar em json

url_cria = "https://api.themoviedb.org/3///discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=96275fcac06ba8cbe9d9d4e246f32038"
resposta_cria = urllib.request.urlopen(url_cria)    ##urlopen
dados_cria = resposta_cria.read()                   ##variável para read
jsondata_cria = json.loads(dados_cria)              ##transformar em json

print(jsondata_pop['results'])
print(jsondata_cria['results'])

