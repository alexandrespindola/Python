"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

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

print(f'\n{blue}NÚMEROS PRIMOS{clean}\n')
numero = int(input('Digite um número: '))
print('')
total = 0
for c in range(1, numero +1):
    if numero % c == 0:
        print(f'{blue}', end = ' ')
        total += 1
    else:
        print(f'{magenta}', end = ' ')
    print(f'{c}', end = ' ')
if total > 2:
    print(f'\n\n{clean}O número {numero} é divisível {blue}{total}{clean} vezes e {red}NÃO É NÚMERO PRIMO{clean}')
elif total == 2:
    print(f'\n\n{clean}O número {numero} é divisível {blue}{total}{clean} vezes e {green}É NÚMERO PRIMO{clean}')
elif total == 1:
    print(f'\n\n{clean}O número {numero} é divisível {blue}{total}{clean} vez, apenas por 1, então {red} NÃO É NÚMERO PRIMO{clean}')
