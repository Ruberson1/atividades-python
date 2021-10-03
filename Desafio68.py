from random import randint
print('VAMOS JOGAR PAR OU IMPAR?')
v = 0
while True:
    computador = randint(0,10)
    jogador = int(input('Escolha um numero: '))
    total = jogador + computador
    p = ' '
    while p not in 'PpIi':
        p = input('Escolha Par ou Impar [P/I]: ').strip()
    print(f'Voce jogou {jogador} e o computador {computador} total {total}')
    if p == 'Pp':
        if total % 2 == 0:
            print('Voce venceu')
            v += 1
        else:
            print('Voce perdeu')
            break
    elif p == 'Ii':
        if total % 2 == 1:
            print ('Voce Venceu')
            break
        else:
            if total % 2 == 0:
                print('Voce Perdeu')
                break
    print('Vamos Jogar Novamente?...')
print(f'GAME OVER ! Voce venceu {v} vezes ')