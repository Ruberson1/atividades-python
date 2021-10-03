cont = soma = 0
while True:
    n = int(input('Digite qualquer valor: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} numeros e a soma foi {soma}')