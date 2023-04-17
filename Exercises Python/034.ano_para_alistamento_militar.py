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

idade = int(input('Digite a sua idade: '))
if idade <= 17:
    print(f'Você tem {green}{idade}{clean} anos, ainda vai se alistar.')
elif idade == 18:
    print(f'Você tem {green}{idade}{clean} anos, é hora de se alistar!')
else:
    print(f'Você tem {red}{idade}{clean} anos, já passou do tempo de se alistar!')
