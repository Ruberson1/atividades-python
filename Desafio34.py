s = float(input('Qual o salário do funcionário? R$  '))
if s <= 1250:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 /100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(s,novo))