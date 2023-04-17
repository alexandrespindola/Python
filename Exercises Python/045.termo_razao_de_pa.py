"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão."""
   
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

print(f'\n{blue}EXERCÍCIO 51 - PROGRESSÃO ARITMÉTICA{clean}\n')
soma = 0
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
decimo_termo = termo + ((10 - 1)*razao)
print('')
for c in range(termo, decimo_termo + razao, razao):
    print(c, end = ' → ')
    soma += c
print('ACABOU')
print(f'\nA soma dos 10 primeiros termos da PA é {green}{soma}{clean}')
