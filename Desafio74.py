from random import randint
maior = menor = 0
r = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),
randint(1,10))
print('Os valores sorteados foram: ', end=' ')
for n in r:
    print(f'{n}',end=' ')
print(f'O maior valor sorteado foi {max(r)}')
print(f'O menor valor sorteado foi {min(r)}')
