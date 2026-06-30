print("Bem vindo ao sistema de notas da escola!")

notas = []

conceitos = (
    (9, "A"),
    (7, "B"),
    (6, "C"),
    (0, "D")
)

while True:
    recebe_nota = int(input("Insira a nota dos alunos (-1 para sair): "))

    if recebe_nota == -1:
        break
    elif recebe_nota >= 0 and recebe_nota <= 10:
        notas.append(recebe_nota)
    else:
        print("Valor inválido")

for nota in notas:
    media = sum(notas) / len(notas)

for num, conc in conceitos:
    if media >= num:
        print(F"Seu conceito foi {conc}")   
        break
    

    
   
