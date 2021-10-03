from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range (1,8):
    nasc = int(input('Digite o {}º ano de nascimento: '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print ('São {} pessoas maiores de idade'.format(totmaior))
print ('E {} pessoas menores de idade'.format(totmenor))
