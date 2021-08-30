# Faça um programa que leia um número inteiro positivo N e imprima "S" se for um número perfeito e "N" caso contrário.
# Um número é perfeito se for igual à soma de seus divisores positivos diferentes de N.
# Por exemplo, 6 é perfeito, pois 1 + 2 + 3 = 6.

def perfeito():
    n = int(input())
    soma = 0

    for i in range(1, n):
        if n % i == 0:
            soma = soma + i 
    
    if soma == n:
        return print('S')
    else:
        return print('N')

perfeito()