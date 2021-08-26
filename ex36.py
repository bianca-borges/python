"""
Faça um programa que leia um número inteiro e positivo X. Após isso, leia sucessivos números inteiros positivos,
até que um número negativo seja lido. Ao fim, escreva o número de vezes que o número X foi lido do usuário.
"""

n = int(input())

lista = []
cont = 0

while True:
    n1 = int(input())
    if n1 >= 0:
        lista.append(n1)
    else:
        break


for i in range(len(lista)):
    if n == lista[i]:
        cont += 1
    else:
        cont += 0
    i += 1

print(cont)
