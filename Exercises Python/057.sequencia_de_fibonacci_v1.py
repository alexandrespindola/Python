"""Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8"""

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

print(f'\n{blue}SEQUÊNCIA DE FIBONACCI v1.0{clean}\n')
count = 1
count_menos_um = 1
count_menos_dois = 0
numero = int(input('Digite um número maior que zero: '))
if numero >= 3:
    contagem = 3
    print('')
    print('0 → 1', end = ' → ')
    while contagem <= numero:
        print(count, end = ' → ')
        count_menos_dois = count_menos_um
        count_menos_um = count
        count = count_menos_um + count_menos_dois
        contagem += 1
    print(f'{green}ACABOU{clean}')
elif numero == 2:
    print('')
    print('0 → 1', end = ' → ')
    print(f'{green}ACABOU{clean}')
elif numero == 1:
    print('')
    print('0', end = ' → ')
    print(f'{green}ACABOU{clean}')
while numero == 0:
    print(f'\n{red}COMANDO INVÁLIDO!{clean} Tente novamente.\n')
    numero = int(input('Digite um número maior que zero: '))
    if numero >= 3:
        contagem = 3
        print('')
        print('0 → 1', end = ' → ')
        while contagem <= numero:
            print(count, end = ' → ')
            count_menos_dois = count_menos_um
            count_menos_um = count
            count = count_menos_um + count_menos_dois
            contagem += 1
        print(f'{green}ACABOU{clean}')
    elif numero == 2:
        print('')
        print('0 → 1', end = ' → ')
        print(f'{green}ACABOU{clean}')
    elif numero == 1:
        print('')
        print('0', end = ' → ')
        print(f'{green}ACABOU{clean}')
