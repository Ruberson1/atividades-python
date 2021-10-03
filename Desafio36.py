#Aprovar emprestimo bancario para compra de casa
# perguntar Valor Salario idade
#Calcule prestação mensal sem exceder 30% do salário
s = int(input('Digite valor do salário: '))
c = int(input('Digite valor do imóvel: '))
t = int(input('Digite prazo em meses: '))
p = c / t

if p > s * 30/100:
    print('NEGADO, prestação de R$ {:.2f} excede limite de 30%'.format(p))
else:
    print('APROVADO, prestação será de {:.2f}'.format(p))