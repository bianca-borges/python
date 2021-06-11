"""
Locadora de Veículos
"""

import datetime

# --------------- Início menus -----------------------------


def menuprincipal():
    print('|-----------------------------------|')
    print('|           Menu principal          |')
    print('|-----------------------------------|')
    print('\nEscolha uma das opções abaixo: ')
    print('Gerenciar Veículos ..........1')
    print('Gerenciar Clientes ..........2')
    print('Relatórios ..................3')
    print('Sair ........................0')
    op = input('-> ')
    return op


def menuveiculos():
    print("\nGerenciar Veiculos")
    print("   Inserir veiculo.............1")
    print("   Listar veiculos.............2")
    print("   Pesquisar veiculo...........3")
    print("   Atualizar veiculo...........4")
    print("   Remover veiculo.............5")
    op_veiculos = input("-> ")
    return op_veiculos


def menuclientes():
    print("\nGerenciar Clientes")
    print("   Cadastrar Cliente...........1")
    print("   Listar Clientes.............2")
    print("   Pesquisar Cliente...........3")
    print("   Atualizar Cliente...........4")
    print("   Remover Cliente.............5")
    op_clientes = input("-> ")
    return op_clientes


def submenu():
    print('\n Relatórios')
    print("   Exibir modelo mais existente.....1")
    print("   Exibir todos os carros...........2")
    print("   Exibir carros antigos............3")
    print("   Exibir carros novos..............4")
    print("   Exibir clientes .................5")
    print("   Carros sem IPVA .................6")

    op_submenu = input('-> ')
    return op_submenu

# --------------- Fim menus --------------------------------

# ----------- Início reletório -----------------------------


def relatorios1(veiculos_modelo):
    d = {}

    for i in veiculos_modelo:
        d[i] = d.get(i, 0) + 1
    print('|-------------------------------|')
    print('|     Modelo mais existente:    |')
    print('|-------------------------------|\n')
    print(max(d, key=d.get))


def relatorios2(veiculos_modelo):
    d = {}

    for i in veiculos_modelo:
        d[i] = d.get(i, 0) + 1

    print('|-------------------------------|')
    print('|      Carros disponíveis:      |')
    print('|-------------------------------|\n')
    for i in d:
        print(i, d[i], 'unidades disponíveis')


def relatorios3(lista, veiculos_ano):
    cont = 0
    j = 0

    minimo = min(veiculos_ano, key=int)

    for i in veiculos_ano:
        if minimo == i:
            cont += 1

    teste1 = [i[j + 1] for i in lista if i[2] == minimo]
    teste2 = [i[j] for i in lista if i[2] == minimo]

    if cont > 0:
        print('|-----------------------|')
        print('|Carro(s) mais antigo(s)|')
        print('|-----------------------|\n')
        while cont > 0:
            print(f'Modelo: {teste1[j]}')
            print(f'Código: {teste2[j]}')
            print(f'Ano: {minimo}')
            print()
            j += 1
            cont -= 1


def relatorios4(lista, veiculos_ano):
    cont = 0
    j = 0

    maximo = max(veiculos_ano, key=int)

    for i in veiculos_ano:
        if maximo == i:
            cont += 1

    teste1 = [i[j + 1] for i in lista if i[2] == maximo]
    teste2 = [i[j] for i in lista if i[2] == maximo]

    if cont > 0:
        print('|-----------------------|')
        print('| Carro(s) mais novo(s) |')
        print('|-----------------------|\n')
        while cont > 0:
            print(f'Modelo: {teste1[j]}')
            print(f'Código: {teste2[j]}')
            print(f'Ano: {maximo}')
            print()
            j += 1
            cont -= 1


def relatorios5(clientes_nasc):
    jovem = 0
    adulto = 0
    idoso = 0

    date = datetime.date.today()

    for i in clientes_nasc:
        if 18 <= date.year - i <= 23:
            jovem += 1
        elif 24 <= date.year - i <= 69:
            adulto += 1
        elif date.year - i >= 70:
            idoso += 1

    p01 = (100 * jovem) / len(clientes_nasc)
    p02 = (100 * adulto) / len(clientes_nasc)
    p03 = (100 * idoso) / len(clientes_nasc)
    print('Jovens: ' + str(jovem) + ', que correspondem a {:.2f}% do total de clientes.'.format(p01))
    print('Adultos: ' + str(adulto) + ', que correspondem a {:.2f}% do total de clientes.'.format(p02))
    print('Idosos: ' + str(idoso) + ', que correspondem a {:.2f}% do total de clientes.'.format(p03))


def relatorios6(veiculos_ano):
    cont = 0

    date = datetime.date.today()
    for i in veiculos_ano:
        if date.year - i > 20:
            cont += 1

    porcent = (100 * cont) / len(veiculos_ano)
    print('Porcentagem de carros isentos de IPVA: {:.2f}%'.format(porcent))


# --------------- Fim relatório --------------------------------

# ----------- Início Veículos ----------------------------------


def busca(lista, elem):
    i = 0
    while i < len(lista):
        if lista[i] == elem:
            return i
        i = i + 1
    return -1


def inserir_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano, lista):
    v_codigo = input("Informe o codigo: ")

    if busca(veiculos_codigo, v_codigo) == -1:
        v_modelo = input("Informe o modelo: ")
        v_ano = int(input("Informe o ano de fabricacao: "))

        veiculos_codigo.append(v_codigo)
        veiculos_modelo.append(v_modelo)
        veiculos_ano.append(v_ano)
        lista.append([v_codigo, v_modelo, v_ano])

        print("\nVeiculo codigo: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(
            v_ano) + " inserido com sucesso")
    else:
        print("Codigo " + v_codigo + " ja esta cadastrado!")


def listar_veiculos(veiculos_codigo, veiculos_modelo, veiculos_ano):
    for i in range(len(veiculos_codigo)):
        v_codigo = veiculos_codigo[i]
        v_modelo = veiculos_modelo[i]
        v_ano = veiculos_ano[i]
        print("\nVeiculo codigo: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano))
    else:
        print('Nenhum veículo foi cadastrado.')


def pesquisar_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano):
    codigo_pesquisar = input("Informe o codigo a ser pesquisado: ")
    indice = busca(veiculos_codigo, codigo_pesquisar)
    if indice != -1:
        v_codigo = veiculos_codigo[indice]
        v_modelo = veiculos_modelo[indice]
        v_ano = veiculos_ano[indice]
        print("\nVeiculo codigo: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano))
    else:
        print("\nVeiculo codigo " + codigo_pesquisar + " nao encontrado")


def atualizar_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano):
    codigo_atualizar = input("Informe o codigo do veiculo a ser atualizado: ")
    indice = busca(veiculos_codigo, codigo_atualizar)
    if indice != -1:
        v_modelo = input("Informe o novo modelo: ")
        v_ano = input("Informe o novo ano de fabricacao:")
        veiculos_modelo[indice] = v_modelo
        veiculos_ano[indice] = v_ano
        print("Veiculo atualizado com sucesso!")
    else:
        print("\nVeiculo codigo " + codigo_atualizar + " nao encontrado")


def remover_veiculo1(lista, indice):
    i = indice
    while i < len(lista) - 1:
        lista[i] = lista[i + 1]
        i = i + 1
    lista.pop()


def remover_veiculo2(lista, indice):
    ultimo_indice = len(lista) - 1
    lista[indice] = lista[ultimo_indice]
    lista.pop()


def remover_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano):
    codigo_remover = input("Informe codigo do veiculo a ser removido: ")
    indice = busca(veiculos_codigo, codigo_remover)
    if indice != -1:
        remover_veiculo2(veiculos_codigo, indice)
        remover_veiculo2(veiculos_modelo, indice)
        remover_veiculo2(veiculos_ano, indice)
        print("Veiculo removido com sucesso!")
    else:
        print("\nVeiculo codigo " + codigo_remover + " nao encontrado")


# ---------------- Fim Veículos -------------------------------

# ---------------- Início Clientes ----------------------------

def inserir_cliente(clientes_cpf, clientes_nome, clientes_nasc):
    c_cpf = input("Informe o CPF: ")

    if busca(clientes_cpf, c_cpf) == -1:
        c_nome = input("Nome do Cliente: ")
        c_nasc = int(input("Ano de Nascimento: "))

        clientes_cpf.append(c_cpf)
        clientes_nome.append(c_nome)
        clientes_nasc.append(c_nasc)
        print("\nCliente: " + c_nome + ", CPF: " + c_cpf + ", nascimento: " + str(
            c_nasc) + "  inserido com sucesso")
    else:
        print("CPF " + c_cpf + " já está cadastrado!")


def listar_clientes(clientes_cpf, clientes_nome, clientes_nasc):
    for i in range(len(clientes_cpf)):
        c_cpf = clientes_cpf[i]
        c_nome = clientes_nome[i]
        c_nasc = clientes_nasc[i]
        print("\nCliente: " + c_nome + ", CPF: " + c_cpf + ", nascimento: " + str(c_nasc))


def pesquisar_cliente(clientes_cpf, clientes_nome, clientes_nasc):
    cpf_pesquisar = input("Informe o CPF a ser pesquisado: ")
    indice = busca(clientes_cpf, cpf_pesquisar)
    if indice != -1:
        c_cpf = clientes_cpf[indice]
        c_nome = clientes_nome[indice]
        c_nasc = clientes_nasc[indice]
        print("\nCliente: " + c_nome + ", CPF: " + c_cpf + ", ano: " + str(c_nasc))
    else:
        print("\nCPF " + cpf_pesquisar + " nao encontrado")


def atualizar_cliente(clientes_cpf, clientes_nome, clientes_nasc):
    cpf_atualizar = input("Informe o CPF: ")
    indice = busca(clientes_cpf, cpf_atualizar)
    if indice != -1:
        c_nome = input("Nome do Cliente: ")
        c_nasc = input("Ano de nascimento:")
        clientes_nome[indice] = c_nome
        clientes_nasc[indice] = c_nasc
        print("Cadastro atualizado com sucesso!")
    else:
        print("\nCliente CPF " + cpf_atualizar + " não encontrado.")


def remover_cliente1(lista, indice):
    i = indice
    while i < len(lista) - 1:
        lista[i] = lista[i + 1]
        i = i + 1
    lista.pop()


def remover_cliente2(lista, indice):
    ultimo_indice = len(lista) - 1
    lista[indice] = lista[ultimo_indice]
    lista.pop()


def remover_cliente(clientes_cpf, clientes_nome, clientes_nasc):
    cpf_remover = input("Informe o CPF a ser removido: ")
    indice = busca(clientes_cpf, cpf_remover)
    if indice != -1:
        remover_cliente2(clientes_cpf, indice)
        remover_cliente2(clientes_nome, indice)
        remover_cliente2(clientes_nasc, indice)
        print("Cliente removido com sucesso!")
    else:
        print("\nCliente CPF " + cpf_remover + " não encontrado.")


# ---------------------- Fim Clientes -------------------------------


def main():

    clientes_cpf = []
    clientes_nome = []
    clientes_nasc = []

    veiculos_codigo = []
    veiculos_modelo = []
    veiculos_ano = []

    lista = []

    opcao = 'x'
    opcao_relatorios = 'x'
    opcao_veiculos = 'x'
    opcao_clientes = 'x'

    while opcao != '0':
        opcao = menuprincipal()
        if opcao == '1':
            opcao_veiculos = menuveiculos()
            if opcao_veiculos == '1':
                inserir_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano, lista)
            elif opcao_veiculos == '2':
                listar_veiculos(veiculos_codigo, veiculos_modelo, veiculos_ano)
            elif opcao_veiculos == '3':
                pesquisar_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano)
            elif opcao_veiculos == '4':
                atualizar_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano)
            elif opcao_veiculos == '5':
                remover_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano)
            else:
                print('Opção inválida!')

        elif opcao == '2':
            opcao_clientes = menuclientes()
            if opcao_clientes == '1':
                inserir_cliente(clientes_cpf, clientes_nome, clientes_nasc)
            elif opcao_clientes == '2':
                listar_clientes(clientes_cpf, clientes_nome, clientes_nasc)
            elif opcao_clientes == '3':
                pesquisar_cliente(clientes_cpf, clientes_nome, clientes_nasc)
            elif opcao_clientes == '4':
                atualizar_cliente(clientes_cpf, clientes_nome, clientes_nasc)
            elif opcao_clientes == '5':
                remover_cliente(clientes_cpf, clientes_nome, clientes_nasc)
            else:
                print('Opção inválida!')

        elif opcao == '3':
            opcao_relatorios = submenu()
            if opcao_relatorios == '1':
                relatorios1(veiculos_modelo)
            elif opcao_relatorios == '2':
                relatorios2(veiculos_modelo)
            elif opcao_relatorios == '3':
                relatorios3(lista, veiculos_ano)
            elif opcao_relatorios == '4':
                relatorios4(lista, veiculos_ano)
            elif opcao_relatorios == '5':
                relatorios5(clientes_nasc)
            elif opcao_relatorios == '6':
                relatorios6(veiculos_ano)
            else:
                print('Opção inválida!')


main()
