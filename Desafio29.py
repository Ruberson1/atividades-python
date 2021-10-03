# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h. mostre uma mensagem dizendo
# que ele foi multado a multa é 7R$ para cada km acima

v = float(input('Qual a velocidade do carro? '))

if v > 80:
    print('Você foi multado, LIMITE EXCEDIDO')
    multa = (v - 80) * 7
    print('Sua multa é de R${:.2f}!'.format(multa))

print('Tenha um bom dia dirija com segurança')