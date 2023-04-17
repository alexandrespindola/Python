cidade = str(input('Digite o nome de uma cidade: ')).strip()
cidade2 = cidade.upper()
cidade3 = cidade2.split()
if cidade3[0] == "SANTO":
    print('Começa com "SANTO"')
else:
    print('Não começa com "SANTO"')
