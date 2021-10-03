#Desenvolva um programa que pergunte  a distancia de uma viagem
#Calcule  o preço da passagem cobrando 0,50 por km e para
# viagens até 200km e 0,45 para viagens mais longas.
d = float(input('Digite a distancia da viagem: '))
print('Você esta prestes a começar uma viagem de {}km'.format(d))
if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))