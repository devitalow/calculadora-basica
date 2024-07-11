def somar(num1, num2):
    soma = num1 + num2
    print(f'O resultado é: {soma}')

def subtrair(num1, num2):
    subtracao = num1 - num2
    print(f'O resultado é: {subtracao}')

def multiplicar(num1, num2):
    multiplicacao = num1 * num2
    print(f'O resultado é: {multiplicacao}')

def dividir(num1, num2):
    divisao = num1 / num2
    print(f'O resultado é: {divisao}')

def menu():
    print('\nOperações possíveis:')
    print('1. Somar')
    print('2. Subtrair')
    print('3. Multiplicar')
    print('4. Dividir')

while True:

    print('Bem vindo a calculadora!')
    continuar = input('Deseja realizar alguma operação matemática? (s/n): ').lower()

    if continuar == 's':
        print('Digite dois números')
        num1 = float(input('Primeiro número: '))
        num2 = float(input('Segundo número: '))

        menu()

        escolha = int(input('Escolha uma opção: '))

        if escolha == 1:
            print('Somando...')
            somar(num1, num2)
            
            continuar = input('Deseja continuar operando? (s/n): ').lower()
            if continuar == 'n':
                break
        
        if escolha == 2:
            print('Subtraindo...')
            subtrair(num1, num2)
            
            continuar = input('Deseja continuar operando? (s/n): ').lower()
            if continuar == 'n':
                break

        if escolha == 3:
            print('Multiplicando...')
            multiplicar(num1, num2)
            
            continuar = input('Deseja continuar operando? (s/n): ').lower()
            if continuar == 'n':
                break

        if escolha == 4:
            print('Dividindo...')
            dividir(num1, num2)
            
            continuar = input('Deseja continuar operando? (s/n): ').lower()
            if continuar == 'n':
                break
        
        if escolha == 5:
            print('Saindo...')
            break
    else:
        print('Saindo...')
        break