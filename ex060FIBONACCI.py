c = n = x = 0
y = 1
print('='*30)
print('  SEQUENCIA DE FIBONACCI  ')
print('='*30)
f = int(input('Quantos termos voce deseja mostrar?'))
while c < f:
    print(n, end=' . ')
    n = x + y
    y = x
    x = n
    c += 1
print('FIM')
