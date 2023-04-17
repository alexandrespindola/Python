"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo."""

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

print(f'\n{blue}TABUADA v3.0{clean}\n')

numero = int(input('Digite um número: '))
while numero >= 0:
    if numero < 0:
        print('')
        print(f'{red}PROGRAMA FINALIZADO{clean}')
        break
    else:
        print('')
        print(f'{green}TABUADA DO {numero}{clean}')
        print('')
        for c in range(1, 11):
            print(f'{numero} x {c} = {green}{numero * c}{clean}')
        print('')
        numero = int(input('Digite um número: '))
print('')
print(f'{red}PROGRAMA FINALIZADO{clean}')
