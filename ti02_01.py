n = int(input())
lista = list(input().split())

lista_cont = [1 for x in range(n)]
for i in range(1, n):
    for j in range(i):
        if lista[i] > lista[j]:
            if lista_cont[j] + 1 > lista_cont[i]:
                lista_cont[i] = lista_cont[j] + 1


print(max(lista_cont))
