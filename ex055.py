# Faça um programa que leia dados de temperatura durante uma semana (7 leituras), armazenando em uma lista.
# Após isso, seu programa deve imprimir quantos dias dessa semana a temperatura esteve acima da média.

lista = list(map(int,input().split()))
soma = 0
cont = 0
for i in lista:
    soma += i
r = soma/len(lista)
for i in lista:
    if i > r:
        cont += 1
print(cont)