"""Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while."""

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

print(f'\n{blue}ARITMÉTICA v2.0{clean}\n')
soma = 0
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
quantidade_termos = int(input('Quantidade termos da PA: '))
termo = primeiro_termo
enesimo_termo = primeiro_termo + ((quantidade_termos - 1)*razao)
print('')
while termo <= enesimo_termo:
    print(termo, end = ' → ')
    soma += termo
    termo += razao
print('ACABOU')
print(f'\nA soma dos {cyan}{quantidade_termos}{clean} primeiros termos da PA é {green}{soma}{clean}')
