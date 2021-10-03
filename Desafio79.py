valores = list()
while True:
    n = (int(input(' Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso')

    else:
        print('Valor duplicado')
    p = input('Quer continuar [S/N] ? ').strip().upper()
    if p in 'Nn':
        break
print ('=-' * 30)
print(f' Voce digitou os valores {valores}')