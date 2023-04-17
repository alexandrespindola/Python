# ----- dic colors -----

cores = {
    'clean': '\033[m', 
    'black30': '\033[30m',
    'red31': '\033[31m',
    'green32': '\033[32m',
    'yellow33': '\033[1;33m',
    'blue34': '\033[1;34m', 
    'magenta35': '\033[35m',
    'cyan36': '\033[36m',
    'grey37': '\033[37m',
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

casa = float(input('Valor da casa (R$): '))
salario = float(input('Salário do solicitante (R$): '))
anos = int(input('Em quantos anos pretende pagar: '))
prestacao = (casa/anos)/12
if prestacao <= 0.3 * salario:
    print(f'O valor da prestação é de: {green}R${prestacao:.2f}{clean}')
else:
    print(f'{grey}EMPRÉSTIMO NEGADO{clean}')
