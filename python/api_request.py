import requests, json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()

cotacoes_dolar = cotacoes['USDBRL']['bid']
cotacoes_euro = cotacoes['EURBRL']['bid']
cotacoes_bit = cotacoes['BTCBRL']['bid']