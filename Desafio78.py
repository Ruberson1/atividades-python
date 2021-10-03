valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f"Digite valor para posição {c}: ")))
    if c == 0:
        maior = menor = valores[0]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('=-' * 30)
print(f'Voce digitou os valores {valores}')


print(f'O maior valor digitado foi o {maior} ')
for i ,v in enumerate(valores):
    if v == maior:
        print(f'nas posições {i}...')
print(f'O menor valor digitado foi {menor} ')
for i ,v in enumerate(valores):
    if v == menor:

        print(f' Nas posições {i}...')
print('=-' * 30)