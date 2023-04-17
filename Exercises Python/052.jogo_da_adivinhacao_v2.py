"""Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

# ----- dic colors -----

cores = {
    'clean': '\033[m', 
    'black30': '\033[30;47m',
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

print(f'\n{blue}JOGO DA ADIVINHAÇÃO v2.0{clean}\n')

import random
import time
numero = random.randrange(0, 11)
print('O computador está pensando em um número de 0 a 10...')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('Pronto! Agora é a sua vez. Qual número você acha que ele escolheu? ')
palpite = int(input())
tentativas = 1
while palpite != numero:
    print('Errou! Tente mais uma vez: ')
    tentativas += 1
    palpite = int(input())
if tentativas == 1:
    print(f'Parabéns, o número é {green}{numero}{clean}, você acertou na {blue}1ª{clean} tentativa!')
elif tentativas > 1: 
    print(f'Parabéns, o número é {green}{numero}{clean}, você acertou depois de {blue}{tentativas}{clean} tentativas!')
