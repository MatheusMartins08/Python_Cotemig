import json

def carregar_dados():
    with open('dados.json', 'r') as f:
        return json.load(f)

def exibir_menu(caes):
    print("\n--- Menu Pet Shop ---")

    for i, cao in enumerate(caes):
        print(f"{i + 1}. {cao['nome']} ({cao['raca']})")

    escolha = int(input("Escolha um cachorro pelo numero: ")) - 1
    return caes[escolha]


def calcular_banho(peso):
    return peso * 2.5