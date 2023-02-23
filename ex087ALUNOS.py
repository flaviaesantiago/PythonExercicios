import time
dados = []
alunos = []
notas = []
while True:
    alunos.append(str(input(f'Aluno: ')))
    notas.append(float(input(f'Primeira nota: ')))
    notas.append(float(input(f'Segunda nota: ')))
    me = (notas[0] + notas[1]) / 2
    notas.append(me)
    alunos.append(notas[:])
    dados.append(alunos[:])
    alunos.clear()
    notas.clear()
    n = str(input(f'Deseja continuar?')).strip().upper()[0]
    if 'N' in n:
        break
print('No.  NOME      MEDIA')
print('===' * 10)
for c in range(len(dados)):
    print(f'{c:<4} {dados[c][0].capitalize():<10} {dados[c][1][2]:<8} \n')
g = 0
while True:
    print('==' * 20)
    time.sleep(1)
    g = int(input('Ver boletim qual aluno? (999 para sair) '))
    if g < len(dados):
        print(f'{dados[g][0].capitalize():<10}\n PRIMEIRA PROVA: {dados[g][1][0]}\n SEGUNDA PROVA: {dados[g][1][1]}')
    if g == 999:
        print('FINALIZANDO...')
        time.sleep(1)
        print('>>> VOLTE SEMPRE <<<')
        break
