import json

def carregar_dados():

    try:
        with open('dados.json', 'r', encoding="utf-8") as f:
            dados = json.load(f)
            return dados
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return{}