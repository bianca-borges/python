# Melhor investimento[1]:
#
# Um banco oferece a seus clientes 3 formas de investimentos: Poupança, LCI e CDB.
# Faça um programa que receba de entrada um número real, representando o valor
# que o cliente deseja investir, e um número inteiro, representando a quantidade de
# meses que o cliente pretende deixar o dinheiro no investimento.
# Seu programa deve escrever na tela o valor que o cliente terá ao término
# do período de investimento em cada produto oferecido pelo banco.
# Em seguida escreva na tela a primeira letra do melhor produto de investimento
# para o valor e tempo escolhidos pelo cliente, em maiúscula
#
#
# Considere as seguintes rentabilidades para cada produto:
#
# Poupança: juros de 0.59% ao mês;
# LCI: juros de 0.86% ao mês;
# CDB: juros de 1.032% ao mês.
# Considere ainda as seguintes situações:
#
# A Poupança e a LCI são isentas de imposto de renda;
# A LCI tem um prazo mínimo de investimento de 6 meses.
# Assim, considere sua rentabilidade igual a 0% se o prazo apresentado pelo cliente for menor do que 6 meses;
# A rentabilidade de um investimento em CDB é tributada pela Receita Federal.
# O valor real que o cliente irá receber será Valor_investido + Rentabilidade – (Imposto * Rentabilidade).
# Você deve deduzir o valor do imposto a ser pago para apresentar o valor real que o cliente terá disponível, caso escolha este tipo de investimento.
# A tributação é determinada pelo tempo de investimento, nos seguintes valores:
# o de 1 a 6 meses: 22,5%;
# o de 7 a 12 meses: 20%;
# o de 13 a 24 meses: 17,5%;
# o acima de 24 meses: 15%;
# Escreva os valores de cada investimento na ordem Poupança, LCI e CDB, com um valor por linha e com 2 casas decimais.

import math

lista = list(map(int, input().split()))
n = float(lista[0])
mes = lista[1]


def poupanca(n, mes):
    juros = float(0.0059)
    montante = n * pow((1 + juros), mes)
    return montante
    
    
def lci(n, mes):
    juros = float(0.0086)
    if mes < 6:
        return n
    else:
        montante = n * pow((1 + juros), mes)
        return montante

def cdb(n, mes):
    juros = 0.01032
    montante = n * pow((1 + juros), mes)
    rendimento = montante - n
 
    if mes >= 1 and mes <= 6:
        leao = 0.225 * rendimento
        valor_real = montante - leao
        
        return valor_real
        
    if mes >=7 and mes <= 12:
        leao = 0.2 * rendimento
        valor_real = montante - leao
        
        return valor_real
    
    if mes >= 13 and mes <=  24:
        leao = 0.175 * rendimento
        valor_real = montante - leao
        
        return valor_real
        
    if mes >= 24:
        leao = 0.15 * rendimento
        valor_real = montante - leao
        
        return valor_real
    
def compara():
    montante_1 = poupanca(n, mes)
    montante_2 = lci(n, mes)
    montante_3 = cdb(n, mes)
    
    maior = ''
    lista = [montante_1, montante_2, montante_3]
    
    if max(lista) == montante_1:
        maior = 'P'
    elif max(lista) == montante_2:
        maior = 'L'
    else:
        maior = 'C'
    
    print('{:.2f}'.format(montante_1))
    print('{:.2f}'.format(montante_2))
    print('{:.2f}'.format(montante_3))
    print(maior)
    


compara()
