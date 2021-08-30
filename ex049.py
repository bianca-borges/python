# Faça um programa que leia um número inteiro N que indica a quantidade de números em um conjunto.
# Em seguida, leia os N números inteiros que compõem esse conjunto.
# Por fim, o programa deve imprimir dois números, que representam os dois maiores
# valores encontrados no conjunto, ordenados de forma decrescente.

n = int(input())
lista = []

while n > 0:
    x = int(input())
    lista.append(x) 
    n-= 1 

lista.sort(reverse = True)

print(lista[0])
print(lista[1])