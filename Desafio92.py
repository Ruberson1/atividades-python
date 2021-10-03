from datetime import  datetime

dados = {}
dados['nome'] = input('Nome: ')
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados ['ctps'] = int(input(' nº ctps  digite 0 se nao tiver: '))
if dados ['ctps'] != 0:
    dados['contratação'] = int(input('Ano da contratação: '))
    dados['salaraio'] = float(input('Salario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('=-' * 30)
for k, v in dados.items():
    print(f'{k} valor tem valor {v}')