# Faça um programa que leia um valor inteiro N.
# Após isso, leia N valores inteiros.
# Em seguida leia um número inteiro X.
# Ao fim escreva o número de vezes que o número X foi lido do usuário.

n = int(input())
cont = 0

valores = list(map(int, input().split()))

n2 = int(input())

for i in range(len(valores)):
    if n2 == valores[i]:
        cont += 1
    else:
        cont += 0
    i += 1

print(cont)
