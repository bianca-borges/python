# Faça um programa que leia um número inteiro não negativo N e imprima "S" se ele é palíndromo e "N" caso contrário.
# Um número é palíndromo quando lido da esquerda para a direita é igual ao ser lido da direita para a esquerda.
# Exemplos: 37173, 1221.
#
# Obs: Faça seu programa utilizando apenas números inteiros.
# Não é permitido converter o número para string

numero = list(input())

def palindromo(numero):
    inicio = 0
    fim = len(numero)-1
    
    for i in range(len(numero)//2):
        if numero[inicio] != numero[fim]:
            return print('N')
        inicio += 1 
        fim -= 1
        
    return print('S')

palindromo(numero)