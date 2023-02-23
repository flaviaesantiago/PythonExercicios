r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
print('Pode formar um triangulo? ')
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('E POSSIVEL!')
    if r1 == r2 == r3:
        print('Esta formado um triangulo equilatero.')
    if r3 != r1 == r2 or r2 != r1 == r3 or r1 != r2 == r3:
        print('Esta formado um triangulo isosceles')
    if r1 != r2 != r3 != r1:
        print('Esta formado um triangulo escaleno')
else:
    print('NAO E POSSIVEL.')
