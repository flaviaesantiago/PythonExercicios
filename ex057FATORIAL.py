r = 1
n = int(input('Quero saber o fatorial de: '))
c = n
print('{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    r *= c
    c -= 1
print('{}'.format(r))
print('O fatorial do numero escolhido e: {}'.format(r))
