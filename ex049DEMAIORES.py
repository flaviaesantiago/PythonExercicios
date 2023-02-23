from datetime import date
x = date.today().year
p = 0
for c in range(1, 8):
    ano = int(input('ano de nascimento da {}º pessoa: '.format(c)))
    if x - ano >= 21:
        p = p + 1
print('Existem {} pessoas de maior e {} pessoas menores de idade '.format(p, (7 - p)))
