# Jogo da Adivinhação V2.0

from random import randint
#
computador = randint(0,10)
#
print('Sou seu computador . . .')
print('Vou pensar em um número de 0 há 10.')
print('Será que você consegue adivinhar, qual foi?')
#
print('XX'*28)
#
acertou = False
palpites = 0 
while not acertou:
    jogador = int(input('Qual é o seu palpite: ')) 
    palpites += 1 
    if jogador == computador:
        acertou = True
    else: 
        if jogador > computador:
            print('Menos... Tente mais uma vez.')
        elif jogador < computador:
            print('Mais... Tente mais uma vez.')
print(f'Certou com {palpites} tentativas, Parabéns!')
        






