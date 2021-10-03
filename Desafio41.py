from datetime import date
nasc = int(input('Digite ano de nascimento: '))
atual = date.today().year
id = atual - nasc
if id <= 9:
    print ('Sua idade é {} sua categoria é MIRIM'.format(id))
elif id <=14 and id > 9:
    print('Sua idade é {} sua categoria é INFANTIL'.format(id))
elif id <=19 and id > 14:
    print('Sua idade é {} sua categoria é JUNIOR'.format(id))
elif id <=25 and id > 19:
    print('Sua idade é {} sua categoria é SENIOR'.format(id))
else:
    id > 25
    print('Sua idade é {} sua categoria é MASTER'.format(id))