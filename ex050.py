# Faça um programa que leia um número inteiro e positivo N.
# Após isso leia N números inteiros.
# Ao fim, imprima 1 se a sequência de números lidos estão ordenados em forma crescente e -1 se estão ordenados de forma decrescente.
# Se não estão ordenados, imprima 0.
# Considere que uma sequência de tamanho N é crescente quando X1 <= X2 <= ... <= XN e
# decrescente quando X1 >= X2 >= ... >= XN.
# No caso desse exercício, se todos os valores lidos forem iguais, considere como um segmento crescente.

n = int(input())

lista = []

for i in range(n):
    v = int(input())
    lista.append(int(v))

e = 1

while e < len(lista):
    if sorted(lista) == lista:
        print(1)
        break
    elif lista[e] == lista[e - 1]:
        print(1)
        break
    elif lista[e] < lista[e - 1]:
        print(-1)
        break
    elif sorted(lista) != lista:
        print(0)
        break
    e += 1


