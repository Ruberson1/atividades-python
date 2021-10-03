n = [[],[]]
for c in range(1,8):
    num=(int(input(f'Digite o {c}º valor: ')))
    if num % 2 == 0:
        n[0].append(num)
    else:
        n[1].append(num)
n[0].sort()
n[1].sort()
print(f'Os valores pares foram {n[0]}')
print(f'Os valores impares foram {n[1]}')