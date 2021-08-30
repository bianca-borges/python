# Faça um programa que leia um valor inteiro N.
# Após isso, leia N valores inteiros.
# A cada valor lido, o programa deve inserir em uma lista A se o valor for par e em uma lista B se o valor for ímpar.
# Ao fim, escreva as duas listas resultantes, na primeira linha a lista A e na segunda a lista B.

n = int(input())
lista = list(map(int,input().split()))

lista_par = []
lista_impar = []

for i in lista:
    if (i % 2) == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print(*lista_par)
print(*lista_impar)