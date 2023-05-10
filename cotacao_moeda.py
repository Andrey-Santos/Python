import json, requests

moedas_disponives = ["USD", "EUR", "BRL", "JPY"]

for moeda in moedas_disponives:
    print(f"-{moeda}")

origem  = input("Moeda de origem: " ).upper()
destino = input("Moeda de destino: ").upper()

if origem and destino in moedas_disponives:
    requisicao = requests.get(f"https://economia.awesomeapi.com.br/{origem}-{destino}")
    cotacao    = requisicao.json()

    print(f"1 {origem} equivale a {float(cotacao[0]['bid']):.2f} {destino}")
else:
    print("Moedas Inválidas")
