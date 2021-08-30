# Faça um programa que leia um número inteiro N e imprima a soma de todos os números primos entre 1 e N (inclusive N).

n = int(input())

soma = 0

for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        soma = soma + i

print(soma)