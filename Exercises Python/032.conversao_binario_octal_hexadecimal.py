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

numero = int(input('Digite um número inteiro: '))
print("""\nEscolha a base de conversão:
      \n1 para binário
      \n2 para octal
      \n3 para hexadecimal
      """)
base = int(input('Base para conversão: '))
if base == 1:
    binario = bin(numero)
    binario_sem_codigo = binario[2:]
    print(f'Binário = {green}{binario_sem_codigo}{clean}')
elif base == 2:
    octal = oct(numero)
    octal_sem_codigo = octal[2:]
    print(f'Octal = {green}{octal_sem_codigo}{clean}')
elif base == 3:
    hexadecimal = hex(numero)
    hexadecimal_sem_codigo = hexadecimal[2:]
    print(f'Hexadecimal = {green}{hexadecimal_sem_codigo}{clean}')
else:
    print(f'{red}Base de conversão não reconhecida, digite novamente.{clean}')
