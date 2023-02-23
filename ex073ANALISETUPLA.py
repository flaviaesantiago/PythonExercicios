tup = ()
for c in range(0, 6):
    lis = int(input('Digite um valor: '))
    tup += tuple([lis])
print(tup)
print(f'O numero 9 apareceu {tup.count(9)} vezes.')
if 3 not in tup:
    print('O numero 3 nao foi digitado em nenhuma posiçao.')
else:
    print(f'O numero 3 foi digitado primeiro na {(tup.index(3) + 1)}ª posicao.')
print(f'Os numeros digitados pares foram: ', end= '')
for n in tup:
    if n % 2 == 0:
        print(n, end=', ')