#Logica peso e altura imc indicar os valores
a = float(input('Digite altura: '))
p = float(input('Digite peso: '))
imc = p / (a * a)
print (imc)
if imc < 18.5:
    print('Abaixo do peso {}'.format(imc))
elif 18.5 <= imc < 25:
    print('Peso ideal {}'.format(imc))
elif 25<= imc  < 30:
    print('Sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Obesidade {}'.format(imc))
else:
    imc >= 40
    print('Obesidade Mórbida')