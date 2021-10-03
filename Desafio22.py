# Ex 22 faça um programa que leia um nome completo
# TODAS AS LETRAS MAIUSCULAS
# TODAS MINUSCULAS
#QTAS LETRAS SEM ESPAÇOS
#QTAS LETRAS O PRIMEIRO NOME

nome = input (('Digite seu nome completo: ')).strip()
frase = nome
print ('Seu nome com letras maiusculas:',frase.upper())
print ('Seu nome com letras minusculas:',frase.lower())
print ('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print ('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('\033[2;31;40mSeu primeiro nome é {} e tem {} letras'.format(separa[0],len(separa[0])))