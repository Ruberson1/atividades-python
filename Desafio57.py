s = str(input('Digite seu sexo: ')).upper().strip()[0]
while s not in 'MmFf':
    s = input('Dados invalidos por favor digite seu sexo: ')
print('sexo {} registrado com sucesso '.format(s))