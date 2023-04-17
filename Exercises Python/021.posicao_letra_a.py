frase = str(input('Digite uma frase: ')).strip().upper()
letra_a = frase.count('A')
posicao_primeira_a = frase.find('A') + 1
posicao_ultima_a = frase.rfind('A') + 1
print(f'Número de vezes que aparece a letra "a": {letra_a}')
print(f'Posição da primeira letra "a": {posicao_primeira_a}')
print(f'Posição da última letra "a": {posicao_ultima_a}')
