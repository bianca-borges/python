"""
O índice de massa corporal (IMC) é uma medida internacional usada para
calcular se uma pessoa está no peso ideal. O IMC é determinado pela
divisão da massa do indivíduo pelo quadrado de sua altura, em que a
massa está em quilogramas e a altura em metros, ou seja: IMC = massa/altura^2.

Faça um programa que leia a massa e altura da pessoa e calcule o IMC dela
"""

peso = float(input())
altura = float(input())

imc = peso / altura ** 2

print("{:.2f}".format(imc))
