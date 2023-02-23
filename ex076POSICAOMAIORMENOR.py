vs = ()
q = int(input('Quantos valores deseja cadastrar?'))
for c in range(q):
    v = int(input(f'Digite o valor da posiçao {c+1}: '))
    vs += tuple([v])
    if c == 0:
        ma = v
        me = v
    if v > ma:
        ma = v
    if v < me:
        me = v

for c in range(q):
    print(f'Na posiçao {c+1}', f' esta o valor {(vs[c])}')
    if vs[c] == ma:
        cma = c
    if vs[c] == me:
        cme = c
print(f'O maior valor foi {ma} na posiçao {cma+1} ')
print(f'O menor valor foi {me} na posiçao {cme+1}')
