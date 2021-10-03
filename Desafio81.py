valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    p = input('Quer continuar [S/N] ? ').strip().upper()

    if p != 'S':
        break
print(f'Voce digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print ('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
