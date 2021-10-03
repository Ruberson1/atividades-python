# M = C (1 + i) ** t
import matplotlib.pyplot as plt
c = int(input('Digite valor do aporte: '))
tj = float(input('Digite taxa de juros % mensal: '))
t = int(input('Digite quantidade em meses: '))
m = c * (1 + (tj/100))** t

l = m - c
print ('''Sua aplicação ira render {}
no periodo de {} meses
Irá te trazer o lucro de {}'''.format(round(m,2),t, round(l,2)))
