s = 0
n = 0
for c in range(1, 10):
    if c % 3 == 0:
        s += c
        n += 1
print('A soma de todos os {} valores divisiveis por 3 eh: {}'.format(n, s))
