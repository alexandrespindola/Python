numero = str(input('Digite um número de 0 a 9999: '))
if len(numero) == 4:
    print(f'Numeral: {numero[3]}')
    print(f'Dezena: {numero[2]}')
    print(f'Centena: {numero[1]}')
    print(f'Milhar: {numero[0]}')
elif len(numero) == 3:
    print(f'Numeral: {numero[2]}')
    print(f'Dezena: {numero[1]}')
    print(f'Centena: {numero[0]}')
elif len(numero) == 2:
    print(f'Numeral: {numero[1]}')
    print(f'Dezena: {numero[0]}')
elif len(numero) == 1:
    print(f'Numeral: {numero[0]}')
