estoque = {
    "monitor": 8,
    "teclado": 2,
    "mouse": 3,
    "Ram": 7,
    "Cabo de rede": 1,
}

for produto, quantidade in estoque.items():
    if quantidade <= 3:
        print(f"ALERTA!! O {produto} tem um estoque menor ou igual à que 3")
    else:
        print(f"{produto}: tem um estoque maior do que 3")    