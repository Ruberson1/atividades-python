from datetime import date
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF:':
        sexo = input('Digite sexo [M/F]: ').strip().upper()[0]
    if idade >= 18:
        tot18 +=1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 +=1
    p = ' '
    while p not in 'SN':
        p = input('Deseja realizar um novo cadastro [S/N]: ').strip().upper()[0]
    if p == 'N':
        break
print('-'* 60)
print(f'Total de pessoas com mais de 18 anos {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos total de {totM20} mulheres com menos de 20 anos cadastradas')