# Faça um programa que leia as dimensões N e M de uma matriz A, representando o número de linhas e colunas respectivamente.
# Após isso, leia N x M valores em apenas uma linha, colocando-os na matriz A.
# Por fim, imprima a matriz em formato matricial.

n = list(map(int, input().split()))
entrada = list(map(int, input().split()))


def imprime(n, entrada):
    matriz = []

    numero_linhas = n[0]
    numero_colunas = n[1]
    contador = 0

    for i in range(numero_linhas):
        linha = []
        for j in range(numero_colunas):
            linha.append(entrada[contador])
            contador = contador + 1
        matriz.append(linha)

    for i in range(numero_linhas):
        for j in range(numero_colunas):
            print(matriz[i][j], '', end='')
        print()


imprime(n, entrada)
