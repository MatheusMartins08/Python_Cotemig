def realizar_saque(contas, numero_conta, valor):
    # 1. Busca a conta na lista (assumindo que contas é uma lista de dicionários)
    for conta in contas:
        if conta['numero'] == numero_conta:
            # 2. Verifica se tem saldo
            if valor <= 0:
                return False, "Valor de saque deve ser maior que zero."
            
            if conta['saldo'] >= valor:
                conta['saldo'] -= valor  # Atualiza o saldo na memória
                return True, f"Saque de R${valor:.2f} realizado com sucesso!"
            else:
                return False, "Saldo insuficiente."
    
    return False, "Conta não encontrada."
