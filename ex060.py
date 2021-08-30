# Faça um programa que leia um valor inteiro N.
# Após isso, leia N valores inteiros.
# Em seguida, seu programa deve imprimir os N valores na ordem inversa que foram lidos.

n = int(input())

lista = list(map(int, input().split()))
lista2 = []

while n != 0:
    lista2.append(lista[n-1])
    n -= 1

print(*lista2)
