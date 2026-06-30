from funcoes import carregar_dados, exibir_menu, calcular_banho
from datetime import datetime



def main():
    caes = carregar_dados()
    cao_escolhido = exibir_menu(caes)

    valor_banho = calcular_banho(cao_escolhido['peso'])

    agora = datetime.now().strftime("%d/%m/%Y %H:%M")

    print("\n" + "="*25)
    print("\n-- Detalhes do Banho --")
    print(f"Horário: {agora}")
    print(f"Raça: {cao_escolhido['raca']}")
    print(f"Peso: {cao_escolhido['peso']} kg")
    print(f"Valor Total: R$ {valor_banho:.2f}")
    print("\n" + "="*25)

if __name__ == "__main__":
    main()