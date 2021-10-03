expr = input('Digite a expressão; ')
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
    else:
        pilha.append(')')
        break
if len(pilha) == 0:
    print('Sua expressao esta correta')
else:
    print('Sua expressão esta errada')