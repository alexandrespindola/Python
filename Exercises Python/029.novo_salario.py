salario = float(input('Salário atual (R$): '))
if (salario > 1250.00):
    print(f'Novo salário: R${salario * 1.1:.2f}')
else:
    print(f'Novo salário: R${salario * 1.15:.2f}')
