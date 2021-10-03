v1 = int(input('Digite primeiro valor: '))
v2 = int(input('Digite segundo valor: '))
v3 = int(input('Digite terceiro valor: '))
# VERIFICANDO MENOR VALOR
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
# VERIFICANDO MAIOR VALOR
maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print('O menor valor digitado é {}'.format(menor))
print('O maior valor digitado é {}'.format(maior))
