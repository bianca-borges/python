"""
Faça um programa que leia uma temperatura em graus
Celsius e converta e escreva o correspondente em
graus Fahrenheit (pesquise como essa conversão é feita).
"""

c = float(input())

f = (((9 / 5) * c)+ 32)

print("{:.2f}".format(f))