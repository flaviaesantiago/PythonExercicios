s = 0
t = 0
for c in range(1, 7):
    n = int(input('{}º valor: '.format(c)))
    if n % 2 == 0:
        s += n
        t += 1
print('A soma dos {} valores pares, sera de: {}'.format(t, s))
