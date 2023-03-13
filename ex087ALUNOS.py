import time
dados = []
while True:
    a = (str(input('Aluno: ')))
    n1 = (float(input('Nota 1: ')))
    n2 = (float(input('Nota 2: ')))
    me = (n1 + n2) / 2
    dados.append([a, [n1, n2], me])
    r = str(input('Deseja continuar?')).strip().upper()[0]
    if 'N' in r:
        break
print(f'Nº.   NOME    MEDIA')
print('===' * 10)
for c, a in enumerate(dados):
    print(f'{c+1:<4} {a[0].capitalize():<10} {a[2]:<8}\n')
while True:
    print('===' * 10)
    time.sleep(1)
    q = int(input('Ver boletim de qual aluno? (999 para sair)'))
    if q == 999:
        print('FINALIZANDO...')
        time.sleep(1)
        print('>>> VOLTE SEMPRE <<<')
        break
    if q <= len(dados):
            print(f'{dados[q-1][0].capitalize()} \nProva 1: {dados[q-1][1][0]} \nProva 2: {dados[q-1][1][1]}')
    else:
        print('Numero invalido. Tente novamente.')