"""Refaça o DESAFIO 35 dos triângulos, 
acrescentando o recurso de mostrar que tipo de triângulo será formado:"""
   
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

a = int(input('Primeira reta: '))
b = int(input('Segunda reta: '))
c = int(input('Terceira reta: '))
if (a + b > c) and (a + c > b) and (b + c > a):
    if (a == b) and (a == c):
        print(f'Essas medidas podem formar um triângulo {green}EQUILÁTERO{clean}')
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print(f'Essas medidas podem formar um triângulo {green}ISÓSCELES{clean}')
    elif (a != b) and (a != c) and (b != c):
        print(f'Essas medidas podem formar um triângulo {green}ESCALENO{clean}')
else:
    print('Essas medidas não podem formar um triângulo.')
