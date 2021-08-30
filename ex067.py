# Faça um programa que leia uma string S e um caractere C.
# Ao fim escreva o número de vezes que o caractere C aparece na string S.

lista = list(input())
caractere = input()

cont = 0

for i in lista:
    if caractere == i:
        cont += 1
    
print(cont)