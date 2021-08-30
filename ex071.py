# Faça um programa que leia as dimensões N e M de uma matriz A, representando o número de linhas e colunas respectivamente.
# Após isso, leia N x M valores em apenas uma linha, colocando-os na matriz A.
# Por fim, o programa deve imprimir a soma de cada linha da matriz.

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

   
    for i in range(numero_colunas):
        soma = 0
        for j in range(numero_linhas):
            soma += matriz[i][j]
        print(soma)


imprime(n, entrada)

