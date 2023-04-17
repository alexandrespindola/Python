"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

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

print(f'\n{blue}MAIOR E MENOR DA SEQUÊNCIA{clean}\n')
lista = []
for pessoa in range (1, 6):
    peso = float(input(f'[{pessoa}] Peso (kg) : '))
    lista.append(peso)
maior_peso = max(lista)
menor_peso = min(lista)
print('')
print(f'Maior peso: {green}{maior_peso:.2f}{clean} kg')
print(f'Menor peso: {green}{menor_peso:.2f}{clean} kg')
