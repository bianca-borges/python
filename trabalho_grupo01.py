qtde_imoveis = int(input("Imóveis vendidos: "))

# listas vazias
lista_valores = []
tipos = [""]*qtde_imoveis
lista = []

#  declaração de variáveis
maior = 0
media = 0
qtde_margem = 0
soma = 0
soma_c = 0
comissao = 0
fazenda = 0
min_fazenda = 0
media_casa = 0
soma_casas = 0

for i in range(qtde_imoveis):
    valores = input("\nInforme o valor de cada imóvel: ")  # entrada de valores
    lista_valores.append(int(valores))

    # calcula a porcentagem das comissões
    if lista_valores[i] <= 250000:
        comissao = (5 / 100) * lista_valores[i]

    elif lista_valores[i] > 250000:
        comissao = (8 / 100) * lista_valores[i]

    soma += lista_valores[i]  # soma de todos os valores dos imóveis
    soma_c += comissao  # soma os valores das comissões

    # checagem de margem de valores
    if 200000 <= lista_valores[i] <= 350000:
        qtde_margem += 1
    else:
        pass

    media = soma / qtde_imoveis  # média imóveis

    tipos[i] = input("Informe o tipo de cada imóvel: ")  # entrada de tipos de imóveis (list)

    lista.append([int(valores), tipos[i]])  # junção de duas listas

    # imóvel mais caro e o seu valor
    maior = lista[0]
    for valor in lista:
        if valor > maior:
            maior = valor

    # fazenda mais cara e o seu valor

    soma_casas = [i[0] for i in lista if i[1] == 'casa']
    media_casa = sum(soma_casas) / len(soma_casas)

    fazenda = [i[0] for i in lista if i[1] == 'fazenda']


print("\nO vendedor vendeu: R${:.2f}".format(soma))
print("Valor total da comissão R${:.2f}".format(soma_c))
print("Imóvel mais caro: R${:.2f}".format(int(maior[0])))
print("Tipo do imóvel mais caro:", maior[1])
print(f"Imóveis que estão entre R$200.000 e R$350.000: {qtde_margem} imóvel(is)")
print("Preço médio dos imóveis: R${:.2f}".format(media))
print("Valor da fazenda mais barata: R${:.2f}".format(min(fazenda)))
print("Valor médio das casas: R${:.2f}".format(media_casa))
