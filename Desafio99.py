from time import sleep
def maior(* num):
    cont = maior = 0
    print('=-' * 30)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor}',end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > 0:
                maior = valor
        cont += 1
    print(f'foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')

# programa principal
maior (2, 9, 4, 3, 7, 1)
maior (4, 2, 0)
maior (1, 2)
maior (6)
maior (0)