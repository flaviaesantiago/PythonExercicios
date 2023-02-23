import time
dados = []
a = []
n = []
while True:
    a.append(str(input('Aluno: ')))
    n.append(float(input('Nota 1: ')))
    n.append(float(input('Nota 2: ')))
    me = (n[0] + n[1]) / 2
    n.append(me)
    a.append(n[:])
    dados.append(a[:])
    a.clear()
    n.clear()
    r = str(input('Deseja continuar?').strip().upper())
    if 'N' in r:
        break
print(f'Nº.   NOME    MEDIA')
print('===' * 10)
for c in range(len(dados)):
    print(f'{c+1:<4} {dados[c][0].capitalize():<10} {dados[c][1][2]:<8}\n')
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
