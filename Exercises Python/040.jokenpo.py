"""Crie um programa que faça o computador jogar Jokenpô com você."""
   
# ----- dic colors -----

cores = {
    'clean': '\033[m', 
    'black30': '\033[30m',
    'red31': '\033[1;97;41m',
    'green32': '\033[97;42m',
    'yellow33': '\033[1;30;43m',
    'blue34': '\033[1;34m', 
    'magenta35': '\033[35m',
    'cyan36': '\033[36m',
    'grey37': '\033[1;30;47m',
    'white97': '\033[4;97m'
    }

clean = cores['clean']
black = cores['black30']
red = cores['red31']
green = cores['green32']
yellow = cores['yellow33']
blue = cores['blue34']
magenta = cores['magenta35']
cyan = cores['cyan36']
grey = cores['grey37']
white = cores['white97']

# -----------------------

import random
import time
print('\nJOKENPÔ\n')
opcoes = [0, 1, 2]
print("""[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")
user = int(input('\nSelecione sua opção: '))
if user == 0 or user == 1 or user ==2:
    computer = random.choice(opcoes)
    print('\nO computador está pensando...\n')
    time.sleep(0.75)
    print('.')
    time.sleep(0.75)
    print('.')
    time.sleep(0.75)
    print('.')
    time.sleep(0.75)
    if user == 0:
        if computer == 0:
            print(f'\nVocê: PEDRA\nComputador: PEDRA\nResultado: {cyan}EMPATE{clean}')
        elif computer == 1:
            print(f'\nVocê: PEDRA\nComputador: PAPEL\nResultado: {red}VOCÊ PERDEU!{clean}')
        elif computer == 2:
            print(f'\nVocê: PEDRA\nComputador: TESOURA\nResultado: {green}VOCÊ GANHOU!{clean}')
    elif user == 1:
        if computer == 0:
            print(f'\nVocê: PAPEL\nComputador: PEDRA\nResultado: {green}VOCÊ GANHOU!{clean}')
        elif computer == 1:
            print(f'\nVocê: PAPEL\nComputador: PAPEL\nResultado: {cyan}EMPATE{clean}')
        elif computer == 2:
            print(f'\nVocê: PAPEL\nComputador: TESOURA\nResultado: {red}VOCÊ PERDEU!{clean}')
    elif user == 2:
        if computer == 0:
            print(f'\nVocê: TESOURA\nComputador: PEDRA\nResultado: {red}VOCÊ PERDEU!{clean}')
        elif computer == 1:
            print(f'\nVocê: TESOURA\nComputador: PAPEL\nResultado:  {green}VOCÊ GANHOU!{clean}')
        elif computer == 2:
            print(f'\nVocê: TESOURA\nComputador: TESOURA\nResultado: {cyan}EMPATE{clean}')
else:
    print('\nSELECIONE A OPÇÃO CORRETA, TENTE OUTRA VEZ')
