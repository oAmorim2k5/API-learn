import requests, json

url = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/aplicacao#!/recursos/CotacaoDolarDia")
url = url.load()
print(url)