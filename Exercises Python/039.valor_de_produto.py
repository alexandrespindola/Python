"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros"""

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

preco = float(input('Digite o preço do produto (R$): '))
print("""\nEscolha a forma de pagamento:
      \n1: À vista (dinheiro ou cheque)
      \n2: À vista no cartão
      \n3: Parcelado em até 2x no cartão
      \n4: Parcelado em 3x ou mais no cartão
      """)
pagamento = int(input('Escolha a condição de pagamento: '))
if pagamento == 1:
    print(f'\nValor final: {green}R${preco * 0.9:.2f}{clean} - À VISTA (DINHEIRO OU CHEQUE)')
elif pagamento == 2:
    print(f'\nValor final: {green}R${preco * 0.95:.2f}{clean} - À VISTA (CARTÃO)')
elif pagamento == 3:
    print(f'\nValor final: {green}R${preco:.2f}{clean} - PARCELADO EM ATÉ 2X NO CARTÃO')
elif pagamento == 4:
    print(f'\nValor final: {green}R${preco * 1.20:.2f}{clean} - PARCELADO EM 3X OU MAIS NO CARTÃO')
