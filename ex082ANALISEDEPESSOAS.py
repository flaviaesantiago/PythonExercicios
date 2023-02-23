vs = []
dados = []
ma = []
me = []
nma = nme = ''
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(vs) == 0:
        mai = men = dados[1]
    vs.append(dados[:])
    for p in vs:
        if p[1] > 90:
            if p[0] not in ma:
                ma.append(p[0])
        elif p[1] < 50:
            if p[0] not in me:
                me.append(p[0])
        if p[1] >= mai:
            mai = p[1]
            nma = p[0]
        elif p[1] <= men:
            men = p[1]
            nme = p[0]
    dados.clear()
    sn = str(input('Deseja continuar?')).strip().upper()[0]
    if sn in 'N':
        break
print(vs)
print(f'{len(vs)} pessoas foram cadastradas.')
print(f'A pessoa mais pesada foi {nma} com {mai}kg.')
print(f'A pessoa mais leve foi {nme} com {men}kg.')
print(f'Lista acima do peso: {ma}')
print(f'Lista abaixo do peso{me}')
