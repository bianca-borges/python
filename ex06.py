"""
Em épocas de crise, comerciantes estão oferecendo descontos para aumentarem suas vendas.
Faça um programa que leia o valor total da compra e um valor de desconto
(de 0 a 100, representando a porcentagem de desconto).
O programa de escrever o valor da compra com o desconto aplicado. Escreva a saída com duas casas decimais.
"""

compra = float(input())
desc = float(input())

valor_final = compra - ((desc / 100) * compra)

print("{:.2f}".format(valor_final))
