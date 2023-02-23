f = int(input('Digite um numero: '))
c = f-1
z = f
while c > 0:
    print('{} X {} = {}'.format(z, c, (z*c)))
    soma = z * c
    c -= 1
    z = soma
print('o fatorial de {} eh: {}.'.format(f, soma))