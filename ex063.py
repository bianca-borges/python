# Faça um programa que leia um valor inteiro N.
# Após isso, leia N valores inteiros colocando-os em uma lista.
# Em seguida, leia dois valores I e J que correspondem duas posições na lista.
# Ao final, o programa deve escrever a soma dos elementos entre I e J,
# incluindo os elementos de I e J. Se I ou J forem posições inválidas na lista, imprimir a mensagem INVALIDO.

n = int(input())
entrada = input().split()
v = input().split()
soma = 0
lista = []
    
for i in range(n):
    elem = int(entrada[i])
    lista.append(elem)
    
v1 = int(v[0])
v2 = int(v[1])

i = v1
j = v2

if v1 < v2:
  i = v1
  j = v2
else:
  i = v2
  j = v1
if j > n-1:
    print("INVALIDO")
else:
    while i <= j:
        soma = soma + lista[i]
        i = i + 1
    print(soma)



