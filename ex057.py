# Faça um programa que leia um valor inteiro N.
# Após isso, leia N valores inteiros, inserindo-os em uma lista de tamanho N.
# Em seguida, seu programa deve imprimir o maior valor informado e a posição dele na lista.
# Se o maior valor foi informado mais de uma vez, imprimir a posição do primeiro

n = int(input())
lista = list(map(int,input().split()))

indice = 0
i = 0

while i < n:
    if lista[i] > lista[indice]:
        indice = i
    i += 1

print(lista[indice])
print(indice)