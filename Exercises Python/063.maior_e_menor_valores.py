"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

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

print(f'\n{blue}MAIOR E MENOR VALORES {clean}\n')
import statistics
lista = []
numero = int(input('Digite um valor: '))
lista.append(numero)
opcao = 'S'
while opcao == 'S':
    print('')
    numero_novo = int(input('Digite um valor: '))
    lista.append(numero_novo)
    print('')
    print(f"""Mínimo: {green}{min(lista)}{clean}
Máximo: {green}{max(lista)}{clean}
Média: {green}{statistics.mean(lista)}{clean}""")
    print('')
    opcao = input(str(f'{cyan}Quer continuar? (S/N):{clean} ')).upper()
print(f'\n{red}PROGRAMA FINALIZADO{clean}')
