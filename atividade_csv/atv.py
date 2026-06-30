import pandas as pd

path = r"H:\Python\atividade.csv\banco_5000_clientes.csv"
arquivo = pd.read_csv(path, sep=",", encoding = "utf8")

arquivo['deposito'] = ""
arquivo['hora_deposito'] = " "

def menu():
    while True:
        print("\n--- SISTEMA BANCÁRIO ---")
        print("1. Buscar contas bancárias")
        print("2. Realizar depósitos")
        print("3. Realizar saques")
        print("4. Atualizar os dados no CSV")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\n-> Buscando contas...")
            # Lógica de busca aqui
        
        elif opcao == "2":
            print("\n-> Iniciando depósito...")
            # Lógica de depósito aqui
            valor = float(input("Quanto deseja sacar? "))
            
        elif opcao == "3":
            print("\n-> Iniciando saque...")
            # Lógica de saque aqui
            
            print("\n--- OPERAÇÃO DE SAQUE ---")
            num_conta = int(input("Digite o número da conta: "))
            
            # Verifica se a conta existe no DataFrame
            if num_conta in arquivo['conta'].values:
                valor_saque = float(input("Digite o valor do saque: "))
                
                # Localiza o saldo atual
                saldo_atual = arquivo.loc[arquivo['conta'] == num_conta, 'saldo'].values[0]
                
                if valor_saque <= 0:
                    print("Erro: O valor deve ser maior que zero.")
                elif valor_saque <= saldo_atual:
                    # Atualiza o saldo no DataFrame (memória)
                    arquivo.loc[arquivo['conta'] == num_conta, 'saldo'] -= valor_saque
                    novo_saldo = arquivo.loc[arquivo['conta'] == num_conta, 'saldo'].values[0]
                    print(f"Saque realizado! Novo saldo: R${novo_saldo:.2f}")
                else:
                    print(f"Saldo insuficiente! Saldo atual: R${saldo_atual:.2f}")
            else:
                print("Conta não encontrada!")
            
        elif opcao == "4":
            print("\n-> Salvando dados no arquivo CSV...")
            # Exemplo básico de escrita em CSV
            dados = [["Conta", "Saldo"], ["123", 1000], ["456", 500]]
            with open('banco_5000_clientes.csv', 'w', newline='') as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerows(dados)
            print("Dados atualizados com sucesso!")

        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")
