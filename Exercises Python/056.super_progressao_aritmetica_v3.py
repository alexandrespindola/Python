"""Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos."""

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

print(f'\n{blue}SUPER PROGRESSÃO ARITMÉTICA v3.0{clean}\n')
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
continuar = int(input(f"""\nVocê quer adicionar mais termos?
{cyan}[ 1 ] SIM
[ 0 ] NÃO{clean}\n
Opção: """))
while continuar != 0 and continuar != 1:
    print(f'\n{red}COMANDO INVÁLIDO!{clean} Tente outra vez.')
    continuar = int(input(f"""\nVocê quer adicionar mais termos?
{cyan}[ 1 ] SIM
[ 0 ] NÃO{clean}\n
Opção: """))
while continuar == 0 or continuar == 1 or continuar > 1: 
    if continuar == 0:
        print('\nPROGRAMA FINALIZADO')
        break
    elif continuar > 1:
        print(f'\n{red}COMANDO INVÁLIDO!{clean} Tente outra vez.')
        continuar = int(input(f"""\nVocê quer adicionar mais termos?
{cyan}[ 1 ] SIM
[ 0 ] NÃO{clean}\n
Opção: """))
    else:
        while continuar == 1:
            novos_termos = int(input('Quantos termos a mais? '))
            nova_quantidade_termos = quantidade_termos + novos_termos
            enesimo_termo = primeiro_termo + ((nova_quantidade_termos - 1)*razao)
            termo = primeiro_termo
            quantidade_termos = nova_quantidade_termos
            soma = 0
            print('')
            while termo <= enesimo_termo:
                print(termo, end = ' → ')
                soma += termo
                termo += razao
            print('ACABOU')
            print(f'\nA soma dos {cyan}{nova_quantidade_termos}{clean} primeiros termos da PA é {green}{soma}{clean}')
            continuar = int(input(f"""\nVocê quer adicionar mais termos?
{cyan}[ 1 ] SIM
[ 0 ] NÃO{clean}\n
Opção: """))
