from random import randint
c = randint (0,10)
print ('''Ola sou seu computador!!
Eu pensei em um numero de 0 a 10''')
print ('Sera que voce consegue acertar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == c:
        acertou = True
    else:
        if jogador < c:
            print ('Mais ... tente outra vez')
        elif jogador > c:
            print('Menos... tente outra vez')

print ('Acertou com {} tentativas Parabens!'.format(palpites))