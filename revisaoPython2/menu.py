from datetime import datetime

def mostrar_data_hora():
    agora = datetime.now()
    return agora.strftime("%d/%m/%Y %H:%M:%S")


def exibir_menu(servicos):
    print("\n === MENU STREAMING ===")
    print(f"Acesso em: {mostrar_data_hora()}")

    for i, servico in enumerate(servicos.keys(), start=1):
        print(f"{i} - {servico}")

    print("0 -Sair")

def escolher_opcao(servicos):
    try:
        opcao = int(input("Escolha uuma opção: "))

        if opcao == 0:
            return 0

        lista_servicos = list(servicos.keys())

        if 1 <= opcao <= len(lista_servicos):
            nome = lista_servicos[opcao - 1]
            preco = servicos[nome]
            print(f"\n{nome}: R$ {preco:.2f}")
        else:
            print("Opção inválida")
    except ValueError:
        print("Digite um número válido")