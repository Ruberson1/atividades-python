def notas(*n, sit=False):
    """
    -> função para analisar notas e situação de varios alunos
    :param n: uma ou mais notas dos alunos aceita varias
    :param sit: valor opcional indicando se deve ou nao informar
    :return: dicionario com varias informações sobre situação do aluno.
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r ['media'] >= 7:
            r['Situação'] = 'BOA'
        elif r['media'] >= 5:
            r['Situação'] ='RAZOAVEL'
        else:
            r['Situação'] = 'RUIM'

    return r

resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
(notas)