"""
Faça um programa que leia um número inteiro E de eleitores de um município,
um número inteiro B que representa o número de votos brancos, um número N de
votos nulos e um número V de votos válidos. O programa deve calcular e
escrever o percentual que cada um representa em relação ao total de eleitores,
além da porcentagem de ausentes. Formate sua saída conforme exemplos abaixo.
"""

e = int(input())
b = int(input())
n = int(input())
v = int(input())

b = (b * 100) / e
n = (n * 100) / e
v = (v * 100) / e
a = 100 - (b + n + v)

print("Nulos: {:.2f}%".format(n))
print("Brancos: {:.2f}%".format(b))
print("Validos: {:.2f}%".format(v))
print("Ausentes: {:.2f}%".format(a))