nome = str(input('Digite seu nome completo: ')).strip().title()
nome_split = nome.split()
len(nome_split)
print(f'Primeiro nome: {nome_split[0]}')
print(f'Último nome: {nome_split[-1]}')
