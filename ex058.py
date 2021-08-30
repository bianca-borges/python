# Faça um programa que leia um valor inteiro N.
# Após isso, leia N valores inteiros.
# Em seguida leia um número inteiro X.
# Ao fim escreva a primeira posição na lista em que o valor X foi encontrado.
# Se X não estiver na lista, escrever -1.

n = int(input())

lista = list(map(int, input().split()))

n2 = int(input())

def busca(lista, n2):
    contador = 0
    for i in lista:
        if n2 != i:
            contador += 1 
        else:
            return print(contador)
        if n2 not in lista:
            return print(-1)
        
busca(lista, n2)
        