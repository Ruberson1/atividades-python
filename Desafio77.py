palavras = ('aprender','programar','linguagem','python','curso','estudar','praticar')
for p in palavras:
    print(f'\n Na palvra {p.upper()} temos: ', end= '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')