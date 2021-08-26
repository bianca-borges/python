# Faça um programa que leia um número inteiro N.
# Após isso leia N datas no formato "dd/mm/aaaa".
# Seu programa deve escrever todas as datas no formato textual "dd de MMM de aaaa".
# Caso a data seja inválida, seu programa deve escrever "DATA INVALIDA".
# Utilize registro para definir a data.

class data:
  
  dia = 0
  mes = 0
  ano = 0
  ano_aux = ""
  dia_aux = ""

datas = []
limite = int(input())

for x in range(limite):
  
  data_string = input().split("/")
  data1 = data()
  data1.dia = int(data_string[0])
  data1.mes = int(data_string[1])
  data1.ano = int(data_string[2])
  data1.ano_aux = data_string[2]
  data1.dia_aux = data_string[0]
  datas.append(data1)

for i in range(limite):
  
  verifica = 1
    
  if datas[i].mes < 1 or datas[i].mes > 12 or datas[i].ano <= 0:
    verifica = 0
        # verifica qual o último dia do mês
  if datas[i].mes in (1, 3, 5, 7, 8, 10, 12):
    ultimo_dia = 31
  elif datas[i].mes == 2:
    if(datas[i].ano % 4 == 0) and (datas[i].ano % 100 != 0 or datas[i].ano % 400 == 0):
      ultimo_dia = 29
    else:
      ultimo_dia = 28     
  else:
    ultimo_dia = 30
        # verifica se o dia é válido
  if datas[i].dia < 1 or datas[i].dia > ultimo_dia:
    verifica = 0
    
  if verifica == 1:
    if datas[i].mes == 1:
      print(datas[i].dia_aux,"de janeiro de",datas[i].ano_aux)
    elif datas[i].mes == 2:
      print(datas[i].dia_aux,"de fevereiro de",datas[i].ano_aux)
    elif datas[i].mes == 3:
      print(datas[i].dia_aux,"de marco de",datas[i].ano_aux)
    elif datas[i].mes == 4:
      print(datas[i].dia_aux,"de abril de",datas[i].ano_aux)
    elif datas[i].mes == 5:
      print(datas[i].dia_aux,"de maio de",datas[i].ano_aux)
    elif datas[i].mes == 6:
      print(datas[i].dia_aux,"de junho de",datas[i].ano_aux)
    elif datas[i].mes == 7:
      print(datas[i].dia_aux,"de julho de",datas[i].ano_aux)
    elif datas[i].mes == 8:
      print(datas[i].dia_aux,"de agosto de",datas[i].ano_aux)
    elif datas[i].mes == 9:
      print(datas[i].dia_aux,"de setembro de",datas[i].ano_aux)
    elif datas[i].mes == 10:
      print(datas[i].dia_aux,"de outubro de",datas[i].ano_aux)
    elif datas[i].mes == 11:
      print(datas[i].dia_aux,"de novembro de",datas[i].ano_aux)
    else:
      print(datas[i].dia_aux,"de dezembro de", datas[i].ano_aux)
  else:
    print("DATA INVALIDA")        
    
  


  
