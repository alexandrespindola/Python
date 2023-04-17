nome = str(input('Digite seu nome completo: ')).strip()
nome2 = nome.upper()
nome3 = nome2.split()
if 'SILVA' in nome3:
    print('Você tem o nome "SILVA"! :)')
else:
    print('Você não tem o nome "SILVA". :(')
