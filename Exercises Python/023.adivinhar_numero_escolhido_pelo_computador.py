import random
import time
numero = random.randrange(0, 6)
print('O computador está pensando em um número de 0 a 5...')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('Pronto! Agora é a sua vez. Qual número você acha que ele escolheu? ')
tentativa = int(input())
if tentativa == numero:
    print(f'Parabéns, o número é {tentativa}, você acertou!')
else:
    print(f'O número escolhido pelo computador foi {numero}.\nTente mais uma vez!')
