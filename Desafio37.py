# escreva um numero inteiro qualquer e peça para o
#usuario escolher qual sera a base de conversão
num = int(input('Digite o numero: '))
print('''Escolha uma das bases para conversão
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1 :
    print('{} convertido para binário é igual á {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print ('{} convertido para oct é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexdec é {}'.format(num,hex(num)[2:]))