""""
Faça um programa que leia um número natural N e imprima
o número harmônico de ordem N. Um número harmônico H é definido por:

H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N

Imprima o resultado com 4 casas decimais.
"""

n = int(input())
soma = 0

for i in range(1, n + 1):
    soma += 1 / i

print("{:.4f}".format(soma))
