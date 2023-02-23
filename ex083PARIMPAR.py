vs = []
vp = []
vi = []
q = int(input('Quantos valores deseja digitar?'))
for c in range(q):
    vs.append(int(input(f'Digite o valor {c+1}:')))
for v in vs:
    if v % 2 == 0:
        if v not in vp:
            vp.append(v)
    else:
        if v not in vi:
            vi.append(v)
print(f'Lista total: {vs}')
print(f'Lista par: {sorted(vp)}')
print(f'Lista impar: {sorted(vi)}')
