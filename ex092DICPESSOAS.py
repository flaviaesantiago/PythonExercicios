dados = {}
pessoas = []
n = ''
me = 0
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados["sexo"] = str(input('Sexo: ')).strip().upper()[0]
        if dados["sexo"] in 'MF':
            break
        print('Por favor digite um "sexo" valido.')
    dados['idade'] = int(input('Idade: '))
    while True:
        n = str(input('Deseja continjuar?[S/N]: ')).strip().upper()[0]
        if n in 'SN':
            break
        print('ERRO. Tente novamente.')
    pessoas.append(dados.copy())
    if n == 'N':
        break
print('=-' * 20)
print(f'{len(pessoas)} pessoas foram cadastradas. ')
for p in range(0, len(pessoas)):
    me += pessoas[p]["idade"]
me = me / len(pessoas)
print(f'A media de idade foi de {me} anos.')
print('=-' * 20)
print('Lista de mulheres:')
if'F' not in dados.values():
    print('Nenhuma mulher foi cadastrada.')
for p in range(0, len(pessoas)):
    if pessoas[p]["sexo"] in 'F':
        print(f'- {pessoas[p]["nome"].capitalize()}')
print('=-' * 20)
print('Pessoas acima da media de idade:')
for p in range(0, len(pessoas)):
    if pessoas[p]["idade"] > me:
        print(f'- {pessoas[p]["nome"].capitalize()} com {pessoas[p]["idade"]} anos.')
