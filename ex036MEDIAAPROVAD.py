print('- - - -' * 5)
print('BOLETIM FINAL')
print('- - - -' * 5)
n1 = float(input('Primeira prova: '))
n2 = float(input('Segunda prova: '))
m = (n1 + n2) / 2
print('- - - -' * 5)
print(' Media de {:.1f}'.format(m))
if m < 5.0:
    print(' REPROVADO ')
elif 5 <= m < 6.9:
    print(' EM RECUPERAÇAO')
else:
    print('APROVADO')
print('- - - -' * 5)
