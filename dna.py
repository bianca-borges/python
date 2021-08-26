# Uma molécula de DNA é uma dupla hélice formada por duas fitas compostas
# por uma sequência de quatro nucleotídeos: citosina (C), timina (T),
# adenina (A) e guanina (G). Quando se tem a informação de quais nucleotídeos
# formam uma fita é possível saber qual é a fita complementar, pois o
# nucleotídeo A se liga com T e o nucleotídeo C se liga com G.
# Por exemplo, se uma das fitas for a sequencia TCGACCA, a fita complementar é AGCTGGT.
#
# Faça um programa que leia uma fita de DNA e o imprima com as duas fitas.
# Considere que a sequência lida terá apenas letras maiúsculas.

dna = input().upper()

def duplica(dna):
	dna_ = []
	for i in dna:
		if i == 'T':
			dna_.append('A')
		elif i == 'A':
			dna_.append('T')
		if i == 'C':
			dna_.append('G')
		elif i == 'G':
			dna_.append('C')
	

	return print(''.join(dna_))
	

print(dna)
duplica(dna)