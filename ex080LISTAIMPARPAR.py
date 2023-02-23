p = []
i = []
vs = []
while True:
    v = int(input('Digite um valor:'))
    if v % 2 == 0:
        p.append(v)
    else:
        i.append(v)
    vs.append(v)
    sn = str(input('Deseja continuar?')).strip().upper()[0]
    if sn in 'N':
        break
print(f'A lista completa: {vs}\nA lista par:{p}\nA lista impar: {i}')
