t = int(input('Digite o termo: '))
r = int(input('Dirigite a razão: '))
tm = t
cont = 1
while cont <= 10:
    print('{} > '.format(tm), end='')
    tm += r
    cont =+ 1
print ('FIM')