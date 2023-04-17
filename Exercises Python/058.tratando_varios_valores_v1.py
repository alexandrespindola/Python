"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,  que é a condição de parada. No final, mostre quantos números foram digitados  e qual foi a soma entre eles (desconsiderando o flag)."""

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

print(f'\n{blue}TRATANDO VÁRIOS VALORES v1.0{clean}\n')
cont = 0
lista = []
numero = int(input('Digite um valor: '))
lista.append(numero)
while numero != 999:
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    cont += 1
print(f'Foram digitados {green}{cont}{clean} números antes do 999, com soma total de {green}{sum(lista) - 999}{clean}')
