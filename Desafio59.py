n1 = int(input('Digite valor 1: '))
n2 = int(input('Digite valor 2: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NUMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input(' Qual é a sua opção? '))
    if opção == 1:
        soma =n1 + n2
        print('A soma entre {} e {} é {}'.format(n1,n2,soma))
    elif opção == 2:
        produto = n1 * n2
        print ('O resultado de {} x {} é de {}'.format(n1,n2,produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print ('Entre {} e {} o maior é {}'.format(n1,n2,maior))

    elif opção == 4:
        print('informe os numero novamente: ')
        n1 = int(input('Digite valor 1: '))
        n2 = int(input('Digite valor 2: '))

    elif opção == 5:
        print (' Finalizando')
    else:
        print ('Opção invalida. tente novamente')
    print('=-= '*10)
print(' Fim do programa')
