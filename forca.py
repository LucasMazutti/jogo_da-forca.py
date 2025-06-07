###jogo ds forca 

import random 

def jogar_forca():
	palavras = ['futebol','basquete','tenis','xadrez']
	palavra_secreta = random.choice(palavras)
	tentativas = 7 
	letras_acertadas = []
	erros = 0
	
	while erros < tentativas and not all(letra in letras_acertadas for letra in palavra_secreta):
		exibiçao = [letra if letra in letras_acertadas else '_' for letra in palavra_secreta]
		print("palavra:", ' '.join(exibiçao))
		
		tentativa = input('digite uma letra: ').lower()
		
		if tentativa in palavra_secreta and tentativa not in letras_acertadas:
			letras_acertadas.append(tentativa)
			print('Letra correta!')
		elif tentativa in letras_acertadas:
			print('Você ja tentou essa letra,')
		else:
			erros +=1
			print(f'Letra incorreta! Você ainda tem {tentativas - erros} tentativas, \n')
			
	if all(letra in letras_acertadas for letra in palavra_secreta):
		print(f'parabéns! você acertou a palavra: {palavra_secreta.upper()}')
	else:
		print(f'Fim de jogo! você perdeu. A palavra era: {palavra_secreta.upper()}')
		
while True:
	jogar_forca()
	jogar_novamente = input('Deseja jogar novamente? (sim/nao): ').lower()
	if jogar_novamente != 'sim':
		print('Obrigado por jogar!')
		break
