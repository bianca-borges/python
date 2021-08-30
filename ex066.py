# Faça um programa que leia uma string S, composta apenas por uma palavra.
# Seu programa deve imprimir os caracteres de S na ordem inversa que aparecem em S, separados por espaço.

lista = list(input())
lista_inversa = []

for i in range(len(lista)-1, -1, -1):
    lista_inversa.append(lista[i])

print(*lista_inversa)