# Faça um programa que leia um valor inteiro N.
# Após isso, leia N valores inteiros.
# Em seguida, seu programa deve imprimir os N valores na ordem que foram lidos.

n = int(input())

lista = list(map(int,input().split()))

print(*lista)