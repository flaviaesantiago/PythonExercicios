cd = 0
n = int(input('Digite um numero: '))
for c in range(1, n+1):
    if n % c == 0:
        cd += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
if cd == 2:
    print('\n\033[m{} eh divisivel apenas por 1 e ele mesmo. Portanto eh primo.'.format(n))
else:
    print('\n\033[m{} eh divisivel pelos {} numeros amarelos acima. Portanto nao eh primo'.format(n, cd))
