# Faça um programa que leia duas strings A e B, e imprima 1 se A e B são anagramas e 0, caso contrário.
# Anagrama é a transposição de letras de palavra ou frase para formar outra palavra ou frase diferente.
# Por exemplo: "algoritmo" e “logaritmo” são anagramas. Seu programa deve desconsiderar caracteres de espaço.

lista1 = list(input().replace(" ", ""))
lista2 = list(input().replace(" ", ""))

def anagrama(lista1, lista2):
    if len(lista1) != len(lista2):
        return print(0)
    cont = {}
    for p in lista1:
        if p in cont:
            cont[p] += 1 
        else:
            cont[p] = 1 
    
    for p in lista2:
        if p in cont:
            cont[p] -= 1 
        else:
            cont[p] = 1 
    
    for i in cont:
        if cont[i] != 0:
            return print(0)
    return print(1)
        

anagrama(lista1, lista2)
                
