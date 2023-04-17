distancia = float(input('Distância da viagem (km): '))
if distancia <= 200:
    print(f'Custo da passagem: R${(distancia * 0.5):.2f}')
else:
    print(f'Custo da passagem: R${(distancia * 0.45):.2f}')
