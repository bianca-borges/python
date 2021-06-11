"""
Faça um programa que leia uma sequência de números inteiros do usuário
até que ele digite o valor zero. Quando o valor zero for digitado, o programa
deve imprimir o resultado em três linhas: 1ª linha) Soma dos valores pares
da sequência; 2ª linha) Soma dos valores ímpares da sequência; 3ª linha) soma de todos os valores da sequência.
"""

soma_impar = 0
soma_par = 0
soma = 0
n = c = 0
while True:
    n = int(input())
    if n % 2 == 0:
        soma_par += n
    else:
        soma_impar += n

    if n == 0:
        break
    soma += n

print(soma_par)
print(soma_impar)
print(soma)
