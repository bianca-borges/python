# Faça um programa que leia um valor inteiro N.
# Após isso, leia N valores inteiros colocando-os em uma lista.
# Em seguida, seu programa deve trocar os elementos dos índices adjacentes, par a par.
# Por exemplo, deve ser trocado o elemento do índice 0 com o do índice 1,
# em seguida o elemento do índice 2 com o do índice 3 e assim sucessivamente.
# Por fim, seu programa deve imprimir a lista resultante.

n = int(input())
lista = input().split()

x = 0
while x < n - 1:
    aux = lista[x]
    lista[x] = lista[x+1]
    lista[x+1] = aux

    x = x + 2

for valor in lista:
    print(valor,'', end = '')
        
        
         
    
