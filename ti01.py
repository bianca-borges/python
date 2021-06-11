n = int(input())

lista = []

for i in range(n):
    v = int(input())
    lista.append(v)

e = 1

while e < len([e]):
    if sorted([e]) == lista[e - 1]:
        print(1)
        break
    elif lista[e] == lista[e - 1]:
        print(1)
        break
    elif lista[e] < lista[e - 1]:
        print(-1)
        break
    elif sorted(lista) != lista:
        print(0)
        break
    e += 1
