# Faça um programa que leia um conjunto de valores que correspondem as
# idades de pessoas de uma comunidade. Quando o valor fornecido for um número negativo,
# significa que não existem mais idades para serem lidas. Após a leitura, seu programa deve informar:
#
# A média das idades das pessoas (com duas casas decimais)
# A quantidade de pessoas maiores de idade
# A porcentagem de pessoas idosas (considere quem uma pessoa idosa tem mais de 75 anos) (com duas casas decimais)

lista = []
while True:
    idade = int(input())
    if idade > 0:
        lista.append(int(idade))
    else:
        break
    
soma = 0
media = 0
maior = 0
idoso = 0
porcent = 0

for i in lista:
    soma += i
    if i >= 18:
        maior += 1 
    if i > 75:
        idoso += 1

if len(lista) > 0:
    porcent = (idoso * 100) / len(lista)
    media = soma / len(lista)
else:
    porcent += 0


print('{:.2f}'.format(media))
print(maior)
print('{:.2f}%'.format(porcent))