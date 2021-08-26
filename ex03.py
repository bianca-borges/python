"""
Faça um programa que leia duas notas de provas e calcule e escreva a
média simples delas. Escreva a saída com duas casas decimais.
"""

a = float(input())
b = float(input())

res = (a + b) / 2

print("{:.2f}".format(res))