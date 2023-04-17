"""Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.."""

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

print(f'\n{blue}VALIDAÇÃO DE DADOS{clean}\n')

sexo = str(input(f'Sexo ({blue}M{clean}/{magenta}F{clean}): ')).upper()
while sexo != 'M' and sexo != 'F':
    print(f'{red}Digite novamente{clean}\n')
    sexo = str(input(f'Sexo ({blue}M{clean}/{magenta}F{clean}): ')).upper()
print(f'{green}Sexo definido corretamente{clean}')
