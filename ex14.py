"""
Faça um programa que leia um número inteiro (assuma que esse
número terá 4 digitos obrigatoriamente) e inverta esse número.
Por fim escreva o número invertido. O seu programa deve apenas
manipular números inteiros. Não é permitido usar strings, lista, etc
"""
n = int(input())

if n > 0:
    n1 = n % 10
    n2 = (n // 10) % 10
    n3 = (n // 100) % 10
    n4 = (n // 1000) % 10
    invertido = int("%d%d%d%d" % (n1, n2, n3, n4))

else:
    a = n_a * 10 + invertido
    print(n_a)

print(invertido)
