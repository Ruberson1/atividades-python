ficha = []
while True:

    nome = input('Nome: ')
    nota1 = float(input(' Nota 1: '))
    nota2 = float(input(' Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1 , nota2], media])
    resp = input('Quer continuar ? ')
    if resp in 'Nn':
        break
print('-=' * 30)
for i, a in enumerate(ficha):
    print(f'{'nº':<4}{'a[0]':<10}{a[2]:>8.1f}')