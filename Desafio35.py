print ('-=-'* 20)
print ('Analisador de triangulo')
print('-=-'* 20)
r1 = int(input('Digite comprimento reta1: '))
r2 = int(input('Digite comprimento reta2: '))
r3 = int(input('Digite comprimento reta3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos {} {} {} formam triangulo'.format(r1,r2,r3))
else:
    print('Os segmentos não formam triangulo')