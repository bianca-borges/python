# Faça um programa que leia um número inteiro N e imprima a soma de todos os fatoriais entre 0 e N (inclusive N). Não utilize bibliotecas matemáticas

def soma(n1):
    soma = 1
    for i in range(1, n1 + 1):
        fat = 1
        for j in range(i, 0, -1):
            fat *= j
        soma += fat
    return print (soma)


n1 = int(input())

(soma(n1))