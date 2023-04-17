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

import numpy
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
notas = [nota1, nota2, nota3]
media = numpy.mean(notas)
print(f'Nota final: {media:.1f}')
if media < 5:
    print(f'{red}REPROVADO{clean}')
elif media >= 5 and media < 7:
    print(f'{blue}RECUPERAÇÃO{clean}')    
elif media >= 7:
    print(f'{green}APROVADO{clean}')
