#crie duas notas faça media
n1 = float(input('Digite nota1: '))
n2 = float(input('Digite nota2: '))

media = n1 + n2 / 2
if media < 5.0:
    print('REPROVADO')
elif media <= 5.0 or media < 7.0:
    print('RECUPERAÇÃO')
else:
    media >= 7.0
    print('APROVADO')
print('Sua nota é:' ,media)

