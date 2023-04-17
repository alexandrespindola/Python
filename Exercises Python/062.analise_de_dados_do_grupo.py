"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

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

print(f'\n{blue}ANÁLISE DE DADOS DO GRUPO{clean}\n')
maior18anos = 0
masculino = 0
mulhermenor20anos = 0
continuar = 'S'
while True:
    if continuar == 'S':
        idade = int(input('Digite IDADE: '))
        if idade > 18:
            maior18anos += 1 
        sexo = str(input('Digite SEXO (M/F): ')).upper()
        while sexo != 'M' and sexo != 'F':
            print('')
            print(f'{red}COMANDO INVÁLIDO!{clean} Tente novamente.')
            print('')
            sexo = str(input('Digite SEXO (M/F): ')).upper()
        if sexo == 'M' or sexo =='F':
            if sexo == 'M':
                masculino += 1
            elif sexo == 'F' and idade < 20:
                mulhermenor20anos += 1
        continuar = input('Quer continuar? (S/N): ').upper()
        print('')
    elif continuar == 'N':
        print(f'Pessoas {blue}MAIORES DE 18 ANOS{clean}: {green}{maior18anos}{clean}')
        print(f'Quantidade de {cyan}HOMENS{clean}: {green}{masculino}{clean}')
        print(f'Quantidade de {magenta}MULHERES{clean} com menos de 20 anos: {green}{mulhermenor20anos}{clean}')
        print(f'{cyan}PROGRAMA FINALIZADO{clean}')
        break 
    elif continuar != 'S' and continuar != 'N':
        print('')
        print(f'{red}COMANDO INVÁLIDO!{clean} Tente novamente.')
        continuar = input('Quer continuar? (S/N): ').upper()
        print('')
