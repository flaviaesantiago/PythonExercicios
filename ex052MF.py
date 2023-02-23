m = 0
f = 0
s = str
while s != 'fim':
    s = str(input('Qual seu sexo: [M] [F]: '))
    if s == 'm':
        m += 1
    elif s == 'f':
        f += 1
    if s != 'm' and s != 'f' and s != 'fim':
        print('Dado invalido. Digite novamente seu sexo: ')
print(' Tivemos {} homens e {} mulheres'.format(m, f))