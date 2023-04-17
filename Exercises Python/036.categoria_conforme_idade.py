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

from datetime import date

print('DATA DE NASCIMENTO')
dia = int(input('Dia: ')) 
mes = int(input('Mês: ')) 
ano = int(input('Ano: '))

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

idade = age(date(ano, mes, dia))

print(f'Você tem {idade} anos')

if idade < 9:
    print(f'Sua categoria é {blue}MIRIM{clean}')
elif idade >= 9 and idade < 14:
    print(f'Sua categoria é {blue}INFANTIL{clean}')
elif idade >= 14 and idade < 19:
    print(f'Sua categoria é {blue}JÚNIOR{clean}')
elif idade >= 19 and idade < 25:
    print(f'Sua categoria é {blue}SÊNIOR{clean}')
elif idade > 25:
    print(f'Sua categoria é {blue}MASTER{clean}')
