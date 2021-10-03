#Alistamento
from datetime import date
atual = date.today().year
nasc= int(input('Ano de nascimento: '))
idade = atual - nasc
print ('Quem nasceu em {} tem {} em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Ainda falta {} para o alistamento'.format(saldo))
    print ('Seu alistamento será no ano de {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('voce ja deveria ter se alistado a {} anos'.format(saldo))
    print('Seu alistamento foi no ano de {}'.format(ano))