"""
Faça um programa que leia dois números inteiros N e M e imprima a soma de
todos os números entre eles (inclua N e M na soma). Faça sua solução utilizando laço de repetição.
"""

n = int(input())
m = int(input())

aux = 0

while n <= m:
    aux += n
    n += 1

print(aux)
