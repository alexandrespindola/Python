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

n1 = int(input('Digite primeiro número: '))
n2 = int(input('Digite segundo número: '))
if n1 > n2:
    print(f'{green}O primeiro valor é maior{clean}')
elif n2 > n1:
    print(f'{green}O segundo valor é maior{clean}')
else:
    print(f'{red}Não existe valor maior, os dois são iguais{clean}')
