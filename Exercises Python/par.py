import random

def par_ou_impar():
    lista = [1, 2, 3, 4]
    cont = 0
    while True:
        opcao_pessoa = input('Par ou Ímpar? (P/I): ').upper()
        while opcao_pessoa not in ['P', 'I']:
            opcao_pessoa = input('Opção inválida. Par ou Ímpar? (P/I): ').upper()
        numero_pessoa = int(input('Digite seu número: '))
        while numero_pessoa not in lista:
            numero_pessoa = int(input('Número inválido. Digite um número de 1 a 4: '))
        numero_computador = random.choice(lista)
        soma = numero_computador + numero_pessoa
        resultado = 'P' if soma % 2 == 0 else 'I'
        print(f'Seu número: {numero_pessoa}')
        print(f'Número do computador: {numero_computador}')
        print(f'Soma: {soma}')
        print(f'Resultado: {resultado}')
        if opcao_pessoa == resultado:
            print('VOCÊ GANHOU!')
            cont += 1
            print('')
        else:
            print('VOCÊ PERDEU! O jogo acabou.')
            print(f'Número de vitórias: {cont}!')
            break

par_ou_impar()