akm = float(input('Kilômetros percorridos: '))
dias = int(input('Dias alugados: '))
preço = ((km * 0.15) + (dias * 60))
print(f'Valor total a pagar: R${preço:.2f}')
