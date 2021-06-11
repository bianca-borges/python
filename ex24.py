"""
Faça um algoritmo que leia 3 valores inteiros A, B e C. Coloque-os
em ordem crescente (ou seja, ao final A deve armazenar o menor valor,
C o maior e B o valor do meio). Utilize o modelo abaixo apresentado
no final do exercício, modificando apenas o processamento
"""

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 <= n2 <= n3:
    print(n1)
    print(n2)
    print(n3)

elif n1 <= n3 <= n2:
    print(n1)
    print(n3)
    print(n2)

elif n2 <= n1 <= n3:
    print(n2)
    print(n1)
    print(n3)

elif n2 <= n3 <= n1:
    print(n2)
    print(n3)
    print(n1)

elif n3 <= n2 <= n1:
    print(n3)
    print(n2)
    print(n1)

elif n3 <= n1 <= n2:
    print(n3)
    print(n1)
    print(n2)