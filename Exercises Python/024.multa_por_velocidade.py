velocidade = float(input('Velocidade do carro (km/h): '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Você foi multado!\nA multa vai custar R${multa:.2f}')
else:
    print('Ok, você está indo bem!')
