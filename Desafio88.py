from random import randint
lista = []
jogos = []
print('-' *30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quantos jogos voce quer que eu sorteie? '))
tot = 0
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'Os numeros sorteados foram {jogos}',)

