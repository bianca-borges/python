"""
Faça um programa que leia o salário fixo de um vendedor e o total de
vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor
ganha 18% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês.
"""

sal_fix = float(input())
vendas = float(input())

sal_final = ((18 / 100) * vendas) + sal_fix

print("{:.2f}".format(sal_final))

