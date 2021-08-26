"""
Faça um algoritmo que leia 2 valores inteiros A e B. Coloque-os em ordem crescente
(ou seja, ao final A deve armazenar o menor valor e B o maior valor).
Utilize o modelo abaixo apresentado no final do exercício, modificando apenas o processamento
"""

n1 = int(input())
n2 = int(input())

if n1 <= n2:
    print(n1)
    print(n2)
else:
    print(n2)
    print(n1)

