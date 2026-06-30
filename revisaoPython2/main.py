from leitura_dados import carregar_dados
from menu import exibir_menu, escolher_opcao

def main():
    dados = carregar_dados()

    if not dados:
        return

    while True:
        exibir_menu(dados)
        resultado = escolher_opcao(dados)

        if resultado is 0:
            print("Saindo do sistema...")
            break


if __name__ == "__main__":
    main()