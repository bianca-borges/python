"""
Placar e pontuação de um jogo de boliche:

O boliche é um esporte praticado com uma bola pesada e tem como objetivo lançar a bola por uma pista, derrubar 10 pinos do lado oposto da pista dispostos em formação triangular (https://www.infoescola.com/esportes/boliche/).

A fórmula da contagem de pontos no boliche tem as seguintes variáveis (https://boliche.com.br/esporte-boliche/contagem-dos-pontos-no-boliche/):

Os pontos são a soma dos pinos derrubados.
Exceto quando fizer Strike (derrubar 10 pinos na 1.ª bola) ou Spare (derrubar 10 pinos nas duas bolas jogadas)
Se fizer Strike ganha bônus nas 2 bolas jogadas a seguir. Se fizer Spare ganha bônus na próxima bola jogada. O bônus é igual ao número de pinos derrubados.
O total de 1 partida pode variar de zero a 300 pontos.
A pontuação pode ir de zero (quando nenhum pino é derrubado nas dez jogadas ou “frames”) até o máximo possível de 300 pontos, ou seja, 12 “strikes” consecutivos. Supostamente, como cada partida tem 10 “frames” (jogadas), só seriam possíveis 10 “strikes”. Porém, se o jogador derrubar todos os pinos no primeiro arremesso do 10.º “frame”, tem o direito de jogar mais duas bolas, podendo completar 12 “strikes” numa mesma linha.


Faça um programa que leia a quantidade de pinos derrubados por um praticante de boliche em cada jogada e imprima:

a sequência de pinos derrubados (de acordo com os exemplos de entrada e saída e as anotações de contagem de pontos - https://boliche.com.br/esporte-boliche/contagem-dos-pontos-no-boliche/);
a pontuação final do jogador.

Dica: Para testar seu programa, sugere-se utilizar o seguinte simulador de pontos:

https://www.bowlinggenius.com/ 
"""
def main():

	entrada = input()

	total_pontos = 0
	pontos_acumulados_rodada_atual = 0
	total_jogadas_completas = 0
	primeira_jogada = 1
	saida = ""
	jogadas = entrada.split()
	indice_jogada_atual = 0

	for jogada in jogadas:

		if primeira_jogada:

			total_jogadas_completas = total_jogadas_completas + 1

			if jogada == "10":
				total_pontos = total_pontos + int(jogada) + int(jogadas[indice_jogada_atual + 1]) + int(jogadas[indice_jogada_atual + 2])

				if total_jogadas_completas < 10 :
					saida = saida + "X _ | "
				else:

					if int(jogadas[indice_jogada_atual + 1]) == 10:
						saida = saida + "X X"
					else:
						saida = saida + "X "+jogadas[indice_jogada_atual + 1]+" "

					if int(jogadas[indice_jogada_atual + 2]) == 10:
						saida = saida + " X"
					else:
						saida = saida + jogadas[indice_jogada_atual + 2]

					break
				
				pontos_acumulados_rodada_atual = 0

			else:
				total_pontos = total_pontos + int(jogada)
				saida = saida + jogada + " "
				pontos_acumulados_rodada_atual = pontos_acumulados_rodada_atual + int(jogada)
				primeira_jogada = 0

		else:

			if (pontos_acumulados_rodada_atual + int(jogada)) == 10:
				total_pontos = total_pontos + int(jogada) + int(jogadas[indice_jogada_atual + 1])
				
				if total_jogadas_completas == 10:
					saida = saida + "/ "+jogadas[indice_jogada_atual + 1]	
					break
				else:
					saida = saida + "/ | "

			else:
				total_pontos = total_pontos + int(jogada)
				if total_jogadas_completas == 10:
					saida = saida + jogada
				else:
					saida = saida + jogada + " | "

			pontos_acumulados_rodada_atual = 0
			primeira_jogada = 1

		indice_jogada_atual = indice_jogada_atual + 1

	print(saida)
	print(total_pontos)


main()
