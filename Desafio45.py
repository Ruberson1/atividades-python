#crie jokenpõ
from time import sleep

import random
print ('{:=^20}'.format('JOKENPÔ'))

itens = ('pedra','papel','tesoura')
computador = random.randint(0,2)
print('''[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')

jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')

print('=-' * 11)
sleep(0.5)
print('Computador jogou {}'.format(itens[computador]))
sleep(0.5)
print ('Você escolheu {}'.format(itens[jogador]))

if computador == 0: #Jogou pedra
    if jogador ==0:
        print('EMPATE')

    elif jogador == 1:
        print('VOCÊ VENCEU')

    elif jogador == 2:
        print('VOCÊ PERDEU')

    else:
        jogador > 2
        print('JOGADA INVALIDA')

elif computador == 1: #Jogou papel
    if jogador == 1:
        print('EMPATE')

    elif jogador == 0:
        print('VOCÊ PERDEU')

    elif jogador == 2:
        print('VOCE VENCEU')

    else:
        jogador >2
        print('JOGADA INVALIDA')

elif computador == 2: #Jogou tesoura
    if jogador == 2:
        print('EMPATE')

    elif jogador == 1:
        print('VOCE PERDEU')

    elif jogador == 0:
        print('VOCE VENCEU')

    else:
        jogador > 2
        print('JOGADA INVALIDA')
from time import sleep

