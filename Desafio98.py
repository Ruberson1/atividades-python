from time import sleep


def linha():
    print('=-=' * 20)


def contador(i, f, p):

    print(f' contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f' {cont} ' ,end='')
            sleep(0.5)
            cont += p
        print('Fim')
        linha()
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM')
linha()






contador(1, 10, 1)
contador(10, 0, 2)