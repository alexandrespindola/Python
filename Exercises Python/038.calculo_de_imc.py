"""Desenvolva uma lógica que leia o peso 
e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
de acordo com a tabela abaixo:"""
   
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

peso = float(input('PESO (kg): '))
altura = float(input('ALTURA (m): '))
IMC = peso / (altura**2)
if IMC < 18.5:
    print(f'Seu IMC é {green}{IMC:.1f}{clean}, você está ABAIXO DO PESO')
elif IMC >= 18.5 and IMC < 25:
    print(f'Seu IMC é {green}{IMC:.1f}{clean}, você está no PESO IDEAL')
elif IMC >= 25 and IMC < 30:
    print(f'Seu IMC é {green}{IMC:.1f}{clean}, você está com SOBREPESO')
elif IMC >= 30 and IMC < 40:
    print(f'Seu IMC é {green}{IMC:.1f}{clean}, você está com OBESIDADE')
elif IMC >= 40:
    print(f'Seu IMC é {green}{IMC:.1f}{clean}, você está com OBESIDADE MÓRBIDA')
