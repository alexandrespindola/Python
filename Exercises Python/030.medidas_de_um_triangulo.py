a = int(input('Primeira reta: '))
b = int(input('Segunda reta: '))
c = int(input('Terceira reta: '))
if (a + b > c) and (a + c > b) and (b + c > a):
    print('Sim, essas medidas podem formar um triângulo!')
else:
    print('Essas medidas não podem formar um triângulo.')
