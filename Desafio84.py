temp = []
princ = []
maior = menor = 0
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp [1]
    elif temp[1] > maior:
        maior = temp[1]
    else:
        temp[1] < menor
        menor = temp[1]

    princ.append(temp[:])
    temp.clear()
    resp = input('Quer continuar ? [S/N]: ')
    if resp in 'Nn':
        break
print('=-' *40)
print(f'Ao todo voce cadastrou {len(princ)} pessoas')
print(f'O maior peso foi {maior}.Kg ')
for p in princ:
    if p[1] == maior:
        print(f'Peso de {p[0]}' , end='')
print()
print(f'O menor peso foi {menor}.Kg')
for p in princ:
    if p[1] == menor:
        print(f'Peso de {p[0]}', end='')
