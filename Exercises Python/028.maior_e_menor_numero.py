x = int(input('Primeiro número: '))
y = int(input('Segundo número: '))
z = int(input('Terceiro número: '))
# Teste do menor
if x < y and x < z:
    menor = x
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z
# Teste do maior
maior = x
if y > x and y > z:
    maior = y
if z > x and z > y:
    maior = z
print(f'Menor: {menor}')
print(f'Maior: {maior}')
