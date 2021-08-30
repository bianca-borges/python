# Faça um programa que leia um número inteiro positivo N e imprima a soma dos dígitos desse número.
# Por exemplo, se a entrada for 358, a saída será 16 (3 + 5 + 8).
#
# Obs: Não é permitido transformar os números em strings, ou seja,
# resolva o problema apenas utilizando operações matemáticas válidas.

n = list(input())
soma = 0
for i in n:
    soma += int(i)

print(soma)
