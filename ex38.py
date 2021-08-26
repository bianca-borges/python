"""
Faça um programa que leia um número inteiro positivo N. Após isso o programa deve ler N números
inteiros e ao final da leitura imprimir o maior, menor e a soma dos números lidos.
"""

import math

n = int(input())
lista = []

while n > 0:
    n1 = int(input())
    lista.append(n1)
    n -= 1

print(max(lista))
print(min(lista))
print(sum(lista))