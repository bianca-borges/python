# O senhor Nicola quer comprar melancias para oferecer aos
# seus netos no final de semana. Próximo de sua casa há um
# mercadinho que vende melancia da seguinte forma:
# A primeira melancia é vendida por X reais, a segunda por X − 1 reais, a terceira por X − 2
# e assim por diante até o menor valor de 1 real.
# Por exemplo, se X = 3 e o senhor Nicola quiser comprar 5 melancias, o preço total será 3 + 2 + 1 + 1 + 1 = 8.
#
# Faça um programa que leia dois inteiros N e X que
# indicam respectivamente o número de melancia e o
# valor em reais da primeira melancia. Em seguida imprima o valor total em reais.

lista = list(map(int, input().split()))

def melancia(lista):
    n = lista[0]
    x = lista[1]
    
    s = 0
    c = 0
    
    if n == 1:
        return x 
    else:
        while c < n:
            c = c + 1 
            s = s + x 
            if x != 1:
                x = x - 1 
                if x == 1 and c < n:
                    c = c + 1 
                    s = s + 1 
        return s


print(melancia(lista))
