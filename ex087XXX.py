import time
dados = []
while True:
    alunos = str(input(f'Aluno: '))
    nota1 = float(input(f'Primeira nota: '))
    nota2 = float(input(f'Segunda nota: '))
    me = (nota1 + nota2) / 2
    dados.append([alunos, [nota1, nota2], me])
    n = str(input(f'Deseja continuar?')).strip().upper()[0]
    if 'N' in n:
        break
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('===' * 10)
for c, a in enumerate(dados):
    print(f'{c:<4} {a[0].capitalize():<10} {a[2]:<8} \n')
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