n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero:'))
n3 = int(input('Terceiro numero: '))
m = n1
if n3 < n2 > n1:
    m = n2
if n2 < n3 > n1:
    m = n3
print('O maior valor eh {}.'.format(m))
n = n1
if n3 > n2 < n1:
    n = n2
if n2 > n3 < n1:
    n = n3
print('O menor valor eh {}.'.format(n))
