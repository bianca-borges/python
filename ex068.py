# Faça um programa que leia uma string S e imprima imprima 1 se ela é palíndromo e 0 caso contrário.
# Uma string é palíndromo se quando lido da esquerda para a direita é igual ao ser lido da direita para a esquerda.
# Exemplos: "arara", "amor e roma".
# Observações importantes:
# 1) Seu programa deve desconsiderar caracteres de espaço;
# 2) Seu programa NÃO deve criar uma string auxiliar, ou seja, ele deve dizer se a string é palíndromo apenas acessando/consultando seus caracteres.

palavra = list(input().replace(" ", ""))

def palindromo(palavra):
    inicio = 0
    fim = len(palavra)-1
    
    for i in range(len(palavra)//2):
        if palavra[inicio] != palavra[fim]:
            return print(0)
        inicio += 1 
        fim -= 1
        
    return print(1)

palindromo(palavra)