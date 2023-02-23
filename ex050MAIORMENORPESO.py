m = 0
n = str
t = 0
nomin = str
for c in range(1, 6):
    nome = str(input('Nome {}: '.format(c)))
    peso = float(input('Peso {}: '.format(c)))
    if c == 1:
        m = peso
        t = peso
    if peso > m:
        m = peso
        n = nome
    if peso < t:
        t = peso
        nomin = nome
print(' O mais pesado foi {}, com {}KG.'.format(n, m).capitalize())
print('O mais leve foi {}, com {}KG.'.format(nomin, t).capitalize())
