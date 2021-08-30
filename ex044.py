# Considere que seu computador só consegue realizar operações de soma ou subtração, ou seja,
# está com as operações de divisão e multiplicação inoperantes.
# Faça um programa que leia dois números inteiros positivos A e B,
# onde A é a base e B é o expoente de uma potência. Após isso, calcule o
# valor da potência sem utilizar as operações inoperantes. Imprima o valor de A elevado a B.
#
# Obs: Não utilize bibliotecas matemáticas. No caso de python,
# não é permitido usar o operador **. Faça sua solução utilizando laço de repetição.

def soma(a, b):
    tot = a
    i = 1
    while i < b:
        tot += a
        i += 1
    return tot


def multiplica(b, n=0):
    if n == 0:
        return 1
    tot = b
    i = 1
    while i < n:
        tot = soma(tot, b)
        i += 1
    return tot


a = int(input())
b = int(input())

print(multiplica(a, b))
