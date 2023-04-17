"""Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

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

print(f'\n{blue}GRUPO DA MAIORIDADE{clean}\n')
from datetime import date
atual = date.today().year
individuo = 0
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nasc = int(input(f'{individuo + pessoas}) Digite o ano de nascimento: '))
    idade = atual - nasc
    if idade >= 0:
        print(f'Essa pessoa tem {green}{idade}{clean} anos de idade.')
        if idade >= 18:
            print(f'{green}MAIOR DE IDADE{clean}\n')
            totmaior += 1
        elif idade >= 0 and idade < 18:
            print(f'{red}MENOR DE IDADE{clean}\n')
            totmenor += 1
    else:
        print(f'\n{black}Não nasceu ainda!{clean}\n')
print(f'\nO número de pessoas {green}MAIOR de idade é {totmaior}{clean} e {red}MENOR de idade é {totmenor}{clean}')
