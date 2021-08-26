"""
Faça um programa que leia um número inteiro S que representa uma quantidade de segundos.
Seu programma deve imprimir quatro valores inteiros, que representem a
quantidade de segundos S em dias, horas, minutos e segundos. Por exemplo,
188365 segundos representam 2 dias, 4 horas, 19 minutos e 25 segundos.
Dica: lembre-se dos operadores resto e divisão inteira.
"""

s = int(input())  # 188365


d = s // 86400  # 86400s -> 24 h
h = ((s % 86400) // 3600)  # 3600s -> 1 h
m = ((s % 3600) // 60)
s %= 60


print(d, h, m, s)


