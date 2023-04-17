"""Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""

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

print(f'\n{blue}ESTATÍSTICAS EM PRODUTOS{clean}\n')
total = 0
produto_maior_1000 = 0
valor_anterior = 0
nome_mais_barato = ''
count = 0
continuar = 'S'
while True:
    if continuar == 'S':
        nome_produto = str(input(f'NOME DO PRODUTO {count + 1}: ')).strip().upper()
        preco = float(input('PREÇO (R$): '))
        total += preco
        count += 1
        if preco > 1000:
            produto_maior_1000 += 1
        elif count == 1:
            nome_mais_barato = nome_produto
            valor_anterior = preco
        elif count > 1:
            if preco < valor_anterior:
                nome_mais_barato = nome_produto
        continuar = input('\nQuer continuar? (S/N): ').upper()
        print('')
    elif continuar == 'N':
        print(f'{blue}TOTAL{clean}: {green}R${total:.2f}{clean}')
        print(f'Quantidade de {cyan}PRODUTOS ACIMA DE R$1000{clean}: {green}{produto_maior_1000}{clean}')
        print(f'Produto mais barato: {magenta}{nome_mais_barato}{clean}')
        print(f'{cyan}PROGRAMA FINALIZADO{clean}')
        break 
    elif continuar != 'S' and continuar != 'N':
        print(f'{red}COMANDO INVÁLIDO!{clean} Tente novamente.')
        continuar = input('\nQuer continuar? (S/N): ').upper()
        print('')
