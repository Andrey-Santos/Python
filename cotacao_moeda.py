import json, requests

moedas_disponives = ["USD", "EUR", "BRL", "JPY"]

for moeda in moedas_disponives:
    print(f"-{moeda}")

origem  = input("Moeda de origem: " ).upper()
destino = input("Moeda de destino: ").upper()
valor   = float(input("Valor a ser convertido: "))

if origem and destino in moedas_disponives:
    requisicao = requests.get(f"https://economia.awesomeapi.com.br/{origem}-{destino}")
    cotacao    = float(requisicao.json()[0]['bid'])

    print(f"{valor} {origem} equivale a {float(valor * cotacao):.2f} {destino}")
else:
    print("Moedas Inválidas")
