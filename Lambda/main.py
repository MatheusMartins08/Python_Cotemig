# ATIVIDADE

#1
# O avô de Ana tem o triplo de sua idade. Escreva uma função lambda para calcular a idade do avô, dado a idade de Ana..
# Ana tem 20 anos. Qual a idade do avô?

idadeAna = 20

idadeAvo = lambda x: x * 3


#2
# Dada uma lista de números, use uma função lambda para filtrar apenas os números pares

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

filtro = list(map(
    lambda x: x,
    filter (lambda x: x % 2 == 0, lista)
))
print(filtro)
#3
# Dada uma lista de palavras, use uma função lambda para retornar apenas as palavras que começam com a letra "a"
# use o startswith() para verificar se a palavra começa com "a"

nomes = [arthur, ana, bernardo, matheus, alfredo]


filtroInicio = list(filter(
    lambda x : x.startswith("a") or x.startswith("A"), nomes
))

print(filtroInicio)