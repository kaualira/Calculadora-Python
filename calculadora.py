# Calculadora simples

while True:

    print('\n\t\t\t -- Calculadora -- ')

    print('1. soma')
    print('2. subtração')
    print('3. multiplicação')
    print('4. divisão')
    print('2. sair')

    op = int(input('\n\t Opção: '))

    # Kauã Lira
    if op == 1:
        print('\n\t\t\t -- Soma --\n')
        
        #Entradas
        num1 = int(input('\n\tNum1: '))
        num2 = int(input('\n\tNum2: '))
        
        #Processamento
        resultado = num1 + num2 
        
        #Saída
        print('\n\tResultado: {}'.format(resultado))
    # Kauã Lira
    elif op == 2:
        print('\n\t\t\t -- Subtração --\n')
        
        #Entradas
        num1 = int(input('\n\tNum1: '))
        num2 = int(input('\n\tNum2: '))
        
        #Processamento
        resultado = num1 - num2 
        
        #Saída
        print('\n\tResultado: {}'.format(resultado))
    # Pedro Grechi
    elif op == 3:
        print('\n\t\t\t -- Multiplicação --\n')
        
        #Entradas
        num1 = int(input('\n\tNum1: '))
        num2 = int(input('\n\tNum2: '))
        
        #Processamento
        resultado = num1 * num2 
        
        #Saída
        print('\n\tResultado: {}'.format(resultado))
    # José Luiz - Divisão
    elif op == 4:
        print('\n\t\t\t -- Divisão --\n')
        
        #Entradas
        num1 = int(input('\n\tNum1: '))
        num2 = int(input('\n\tNum2: '))
        
        #Processamento
        resultado = num1 / num2 
        
        #Saída
        print('\n\tResultado: {}'.format(resultado))
    # Kauã Lira
    elif op == 5:
       
        #Saída
        print('\n Forte abraço!\n')
        break
    else:
        print('Opção {} incorreta!'.format(op))