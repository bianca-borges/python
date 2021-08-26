"""
Um matemático italiano da idade média conseguiu modelar
o ritmo de crescimento da população de coelhos através de uma
sequência de números naturais que passou a ser conhecida como
Sequência de Fibonacci. O n-ésimo número da sequência de Fibonacci Fn é
dado pela seguinte formula: Fi = Fi-1 + Fi-2.
O resultado é a sequência {1, 1, 2, 3, 5, 8, 13, 21, ...}.

Faça um programa que leia um número inteiro positivo N e
imprima os N primeiros números da sequência de Fibonacci,
todos em uma linha separados por espaço.
"""

n = int(input())

cont = 1

ant = 1
prox = 1
soma = 1

while cont <= n:
    print(ant, end=' ')
    cont += 1
    soma = prox + ant
    ant = prox
    prox = soma
