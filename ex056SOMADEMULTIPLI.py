r = 0
s = 0
n = int(input('Quero saber a soma das multiplicaçoes de: '))
f = n
while f > 0:
    r = n * f
    s += r
    print('{} X {} = {}'.format(n, f, r))
    f -= 1
print('A soma dos resultados das multiplicaçoes de {} e: {}'.format(n, s))
