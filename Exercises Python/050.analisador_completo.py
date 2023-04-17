"""Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

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

print(f'\n{blue}ANALISADOR COMPLETO{clean}\n')

import statistics
pessoa = 0
lista_nomes = []
lista_sexo = []
lista_idades = []
for pessoa in range (1, 5):
    print(f'PESSOA {pessoa}')
    nome = str(input(f'[{pessoa}] Nome: '))
    lista_nomes.append(nome)
    sexo = int(input(f'[{pessoa}] Sexo [{blue}0 para masculino{clean}, {magenta}1 para feminino{clean}]: '))
    if sexo == 0:
        sexo = 'Masculino'
    elif sexo == 1:
        sexo = 'Feminino'
    lista_sexo.append(sexo)
    idade = int(input(f'[{pessoa}] Idade: '))
    lista_idades.append(idade)
    print('')
print(lista_nomes)
print(lista_sexo)
print(lista_idades)
media_idades = statistics.mean(lista_idades)
print(f'Média das idades: {green}{media_idades}{clean}')
