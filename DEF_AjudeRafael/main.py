estoque = {
    "monitor": 8,
    "teclado": 2,
    "mouse": 3,
    "Ram": 7,
    "Cabo de rede": 1,
}


def mostrar_estoque(estoque):
    print("*******Estoque atual:********")

    for item, quantidade in estoque.items():
        print(item, ":", quantidade)


def saida(a,b):
    item = input("Insira qual item você quer retirar: ")
    retirada = int(input(f"Insira quantos {item} você quer retirar: "))

    for item, quantidade in estoque.items():
        if quantidade >= retirada:
            print(f"Você retirou {retirada} {item}")  
        else:
            print(f"O estoque é insuficiente")



print(saida("monitor", 3))

