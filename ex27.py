"""
Faça um programa que leia dois números inteiros
positivos X e Y e imprima todos os números de X até Y.
Se X for maior que Y, imprima INVALIDO.
"""

x = int(input())
y = int(input())

if x <= y:
    while x <= y:
        print(x)
        x += 1
elif x > y:
    print("INVALIDO")
