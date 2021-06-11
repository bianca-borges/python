"""
Faça um programa que leia o valor dos catetos de um triângulo retângulo e
calcule a hipotenusa, de acordo com o Teorema de Pitágoras.
Pesquise como extrar a raiz quadrada de um número.
"""

a = float(input())
b = float(input())

hip = ((a ** 2) + (b ** 2)) ** 0.5

print("{:.2f}".format(hip))