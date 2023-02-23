vs = ([], [])
valor = 0
q = int(input('Quantos valores deseja digitar?'))
for c in range(q):
    valor = (int(input(f'Digite o valor {c+1}:')))
    if valor % 2 == 0:
        if valor not in vs:
            vs[0].append(valor)
    else:
        if valor not in vs:
            vs[1].append(valor)
print(f'Lista total: {vs}')
print(f'Lista par: {sorted(vs[0])}')
print(f'Lista impar: {sorted(vs[1])}')
