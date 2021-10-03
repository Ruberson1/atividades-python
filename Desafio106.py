c = ('\033[n',     # 0 - sem cores
      '\033[0;30;41n' ,  # 1 - vermelho

     );


def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~'* tam)
    print(c[0], end='')

comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp',1)
    comando = input('Função ou Biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÈ LOGO', 1)
