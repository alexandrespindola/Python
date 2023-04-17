"""Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

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

print(f'\n{blue}JOGO DO PAR OU ÍMPAR{clean}\n')

import random
lista = [1, 2, 3, 4]
cont = 0
while True:
    opcao_pessoa = str(input('Par ou Ímpar? (P/I): ')).upper()
    numero_pessoa = int(input('Digite seu número: '))
    numero_computador = random.choice(lista)
    soma = numero_computador + numero_pessoa
    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    print(f'Seu número: {numero_pessoa}')
    print(f'Número do computador: {numero_computador}')
    print(f'Soma: {soma}')
    print(f'Resultado: {resultado}')
    if opcao_pessoa == resultado:
        print(f'{green}VOCÊ GANHOU!{clean}')
        cont += 1
        print('')
    elif opcao_pessoa != resultado:
        print('')
        print(f'{red}VOCÊ PERDEU! O jogo acabou.{clean}')
        print('')
        print(f'Número de vitórias: {green}{cont}{clean}!')
        break
