import json, requests

origem = "USD"
destino = "BRL"

requisicao = requests.get(f"https://economia.awesomeapi.com.br/{origem}-{destino}")
cotacao = requisicao.json()

print(cotacao[0]["name"])
print(cotacao[0]["bid"])