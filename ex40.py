"""
Na matemática, um número primo é aquele que pode ser dividido somente
por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

Faça um programa que leia um número inteiro positivo N e imprima 1 se ele for primo e 0 caso contrário.
"""


def primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    if n <= 1:
        return False
    return True


n = int(input())

if primo(n):
    print(1)
else:
    print(0)
