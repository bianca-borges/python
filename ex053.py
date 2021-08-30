# Faça um programa que leia um número inteiro N que indica a quantidade de números em um conjunto.
# Em seguida, leia os N números inteiros que compõem esse conjunto.
# O programa deve imprimir o comprimento de um segmento crescente de tamanho máximo.
# Por exemplo, na sequência [3, 7, 4, 3, 6, 8, 9, 2, 5], o segmento crescente máximo é [3, 6, 8, 9], portanto seu comprimento é 4.
# Considere que um segmento de tamanho N é crescente quando X1 <= X2 <= ... <= XN.

n = int(input())
entrada = input().split()

lista = []

for i in range(n):
    elem = int(entrada[i])
    lista.append(elem)

seg = 1 
seg_max = 1 

for i in range(n - 1):
    atual = lista[i]
    proximo = lista[i + 1]
    
    if proximo >= atual:
        seg += 1 
        if seg > seg_max:
            seg_max = seg
    else:
        seg = 1 
        
print(seg_max)