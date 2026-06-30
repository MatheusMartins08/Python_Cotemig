import soma
import subtrair
import multiplicar
import divisao
import potencia
import raizquadrada
import dolar



def calculadora():
    while True:
        
        escolha = input("Escolha o calculo a ser feito: " \
        "\n 0-Sair " \
        "\n 1-soma " \
        "\n 2-subtração " \
        "\n 3-multiplicação " \
        "\n 4-divisão " \
        "\n 5-potência " \
        "\n 6-raizquadrada " \
        "\n 7-Dolar" \
        "\n escolha: ")

        try:
            match escolha:
                case "0":
                    print("Saindo...")
                    break
                case "1":
                    try:
                        n1 = float(input("Insira o primeiro numero: "))
                        n2 = float(input("Insira o segundo numero: "))
                    except ValueError:
                        print("Valor inválido, por favor insira um número.")
                        
                    print(f"A soma de {n1} + {n2} é: {soma.somar(n1,n2)}")
                case "2":
                    try:
                        n1 = float(input("Insira o primeiro numero: "))
                        n2 = float(input("Insira o segundo numero: "))
                    except ValueError:
                        print("Valor inválido, por favor insira um número.")

                    print(f"A subtração de {n1} - {n2} é: {subtrair.subtrair(n1,n2)}")
                case "3":
                    try:
                        n1 = float(input("Insira o primeiro numero: "))
                        n2 = float(input("Insira o segundo numero: "))
                    except ValueError:
                        print("Valor inválido, por favor insira um número.")

                    print(f"A multiplicação de {n1} * {n2} é: {multiplicar.multiplicar(n1,n2)}")
                case "4":
                    try:
                        n1 = float(input("Insira o primeiro numero: "))
                        n2 = float(input("Insira o segundo numero: "))
                    except ValueError:
                        print("Valor inválido, por favor insira um número.")

                    print(f"A divisão de {n1} / {n2} é: {divisao.dividir(n1,n2)}")
                case "5":
                    try:
                        n1 = float(input("Insira o primeiro numero: "))
                        n2 = float(input("Insira o segundo numero: "))
                    except ValueError:
                        print("Valor inválido, por favor insira um número.")

                    print(f"A potência de {n1} ^ {n2} é: {potencia.potencia(n1,n2)}")
                case "6":
                    try:
                        n1 = float(input("Insira o numero: "))
                    except ValueError:
                        print("Valor inválido, por favor insira um número.")
                    print(f"A raiz de {n1} é: {raizquadrada.raizquadrada(n1)}")
                case "7":
                    print(f"O preço atual do dolar é: {dolar.cotacao_dolar()} ")
                    escolha = input("Você deseja converter um valor de real para dolar? S/N: ")
                    if escolha == "S":
                        try:
                            valor = float(input("Insira o valor que deseja converter: "))
                        except ValueError:
                            print("Valor inválido, por favor insira um número.")
                        print(f"O valor {valor} em dolar é: {valor * float(dolar.cotacao_dolar())}" )
                    else:
                        print("Ok") 
                case _:
                        print("Opção inválida.")
        except Exception as e:
            print(f"Erro: {e}")

    
    
