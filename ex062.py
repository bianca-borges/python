# Faça um programa que leia um valor inteiro N.
# Após isso, leia duas listas A e B de tamanho N e coloque a soma das duas listas em uma terceira lista C.
# Por exemplo C[0] = A[0] + B[0], C[1] = A[1] + B[1]. Por fim, imprima a lista resultante C.

n = int(input())
lista = list(map(int, input().split()))
lista_1 = list(map(int, input().split()))
lista_2 = []
i = 0
cont = 0
while i < n:
   soma = lista[i] + lista_1[i]
   lista_2.append(soma)
   i+=1

print(*lista_2)