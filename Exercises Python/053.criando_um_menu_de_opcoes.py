"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

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

print(f'\n{blue}CRIANDO UM MENU DE OPÇÕES{clean}\n')

lista = []
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
lista.append(n1)
lista.append(n2)
print('')
operacao = 0
print(f"""{blue}[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA{clean}""")
print('')
operacao = int(input(f'Digite o número da {blue}OPERAÇÃO{clean} desejada: '))
print('')
while operacao != '':
    if operacao < 1 or operacao > 5:
        print(f'{red}COMANDO INVÁLIDO{clean}. Tente novamente.\n')
        operacao = int(input(f'Digite o número da {blue}OPERAÇÃO{clean} desejada: ')) 
    elif operacao == 1:
        soma_lista = sum(lista)
        print(f'A {blue}SOMA{clean} dos valores é {green}{soma_lista}{clean}')
        print('')
        operacao = int(input(f'Digite o número da {blue}OPERAÇÃO{clean} desejada: '))
    elif operacao == 2:
        produto = 1
        for numero in lista:
           produto *= numero
        print(f'A {blue}MULTIPLICAÇÃO{clean} dos valores é {green}{produto}{clean}')
        print('')
        operacao = int(input(f'Digite o número da {blue}OPERAÇÃO{clean} desejada: '))
    elif operacao == 3:
        maior = max(lista)
        print(f'O {blue}NÚMERO MAIOR{clean} é {green}{maior}{clean}')
        print('')
        operacao = int(input(f'Digite o número da {blue}OPERAÇÃO{clean} desejada: '))
        print('')
    elif operacao == 4:
        novo_numero = int(input(f'Digite um número para {blue}ADICIONAR{clean} à operação: '))
        lista.append(novo_numero)
        print('')
        print(f'{blue}NOVA LISTA{clean} de números: {green}{lista}{clean}')
        print('')      
        operacao = int(input(f'Digite o número da {blue}OPERAÇÃO{clean} desejada: '))
        print('')
    elif operacao == 5:
        print(f'{cyan}PROGRAMA FINALIZADO{clean}')
        break
