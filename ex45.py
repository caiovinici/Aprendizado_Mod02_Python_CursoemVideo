# J O K E N P Ô 
#
from random import randint
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0, 2)
#print(f'Computador jogou {jokenpo[computador]}')
print(' ====  JOKENPÔ  ====')
#
#
print('''\033[33m[0] PEDRA
[1] PAPEL
[2] TESOURA\033[m''')
jogador = int(input('\033[1,40mFaça sua escolha:\033[m'))
print('-=' * 11)
#
#
from time import sleep
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
#
#
print(f'Jogador jogou {jokenpo[jogador]}')
print(f'Computador jogou {jokenpo[computador]}')
print('-=' * 11)
#
if jogador == 0: #PEDRA
    if computador == 1: # PAPEL
        print('Computador \033[32mGANHOU\033[m !')
    elif computador == 2: # TESOURA
        print('Jogador \033[32mGANHOU\033[m !')
    elif computador == 0: # PEDRA
        print('\033[1;40mJogo EMPATADO\033[m X') 
#
if jogador == 1: #Papel
    if computador == 1: #PAPEL
        print('\033[1;40mJogo EMPATADO\033[m ')
    elif computador == 2: #TESOURA
        print('Computador \033[32mGANHOU\033[m !')
    elif computador == 0: # PEDRA
        print('Jogador \033[32mGANHOU\033[m !')

#
if jogador == 2: # Tesoura
    if computador== 1: # PAPEL
        print('Jogador \033[32mGANHOU\033[m !')
    elif computador == 2: # TESOURA
        print('\033[1;40mJogo EMPATADO\033[m X')
    elif computador == 0: # PEDRA
        print('Computador \033[32mGANHOU\033[m !')


