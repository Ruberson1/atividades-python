t = 0
totmil = cont = menor = barato = 0
while True:
    produto = input('Digite nome do produto: ')
    valor = float(input('Digite valor: '))
    t += valor
    if valor >1000:
        totmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto

    s = ' '
    while s not in 'SN':
        s = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if s =='N':
        break

print(f'O total de compras foi {t}')
print(f'Foram {totmil} custando mais de mil reais')
print(f'O valor do produto mais barato é {barato}')
