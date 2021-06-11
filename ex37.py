"""
Faça um programa que leia um número inteiro positivo N. Após isso o
programa deve ler N números inteiros e ao final da leitura imprimir o maior deles.
"""

n = int(input())
m = 0

lista = []

for i in range(n):
    n1 = int(input())
    lista.append(n1)

print(max(lista, key=int))

