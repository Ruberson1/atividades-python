num = cont = soma = 0
num = int(input('Digite numero ou 999 para parar: '))
while num != 999:

    soma += num
    cont += 1
    num = int(input('Digite numero ou 999 para parar: '))
print('Voce digitou {} numeros e a soma foi {}.'.format(cont,soma))