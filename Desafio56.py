idt = 0
media = 0
maioridadehomem = 0
nomevelho = ''
for p in range(1,5):

    print( '-----{}ª pessoa ------'.format(p))
    nome = str(input('Digite nome: ')).strip()
    idade = int(input('Digite idade: '))
    sexo = str(input('Sexo [M/F]: ' )).strip()
    idt += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

media = idt/4

print('A media de idade do grupo é de {} anos: '.format(media))
print ('O homem mais velho tem {} anos e se chama {} '.format(maioridadehomem,nomevelho))