dados = []
a = []
n = []
while True:
    a.append(str(input('Aluno: ')))
    dados.append(a[:])
    n.append(float(input('Nota 1: ')))
    n.append(float(input('Nota 2: ')))
    dados.append(n[:])
    me = (n[0] + n[1]) / 2
    dados.append(me)
    a.clear()
    n.clear()
    r = str(input('Deseja continuar?').strip().upper())
    if 'N' in r:
        break
print(f'Nº.   NOME    MEDIA')
print('==='* 10)
print(dados)
for c in range(len(a)):
    print(f'{c+1}, {dados[c][0]}')
