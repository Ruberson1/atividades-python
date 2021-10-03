pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = pt + (10 -1) * r
for c in range (pt,d + r,r):
    print('{}'.format(c), end=' -> ')
print('Acabou')