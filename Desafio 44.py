#Valor de produto
print ('{:=^40}'.format('LOJAS RUBOM'))
valor = float(input('Digite valor sem desconto: '))
print ('''FORMAS DE PAGAMENTO
[ 1 ] A VISTA DINHEIRO/CHEQUE
[ 2 ] A VISTA CARTÃO
[ 3 ] 2X CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = valor - (valor * 10 / 100)

elif opção == 2:
     total = valor - (valor * 5 / 100)

print(' Sua compra de R$ {:.2f} vai custar R$ {:.2f}no final'.format(valor,total))

elif opção == 3:
     total = valor
     parcela = total / 2
     print('Sua compra será parcelada em duas x de {:.2f}'.format(parcela))
elif opção == 4:
    total = valor + (valor * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros'.format(totparc,parcela))
    print('Sua compra de R$ {2:.f} vai custar R$ {:.2f} no final.'.format(preço, total))