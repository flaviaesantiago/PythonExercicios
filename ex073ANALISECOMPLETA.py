tup = ()
tup2 = ()
list2 = 0
for c in range(4):
    list = int(input('Digite um numero: '))
    tup += tuple([list])
print(tup)
print(f'O numero 9 apareceu {tup.count(9)} vezes')
if 3 not in tup:
    print('O numero 3 nao foi digitado.')
else:
    print(f'O numero 3 apareceu primeiro na {(tup.index(3))+1}ª posiçao ')
for c in tup:
    if c % 2 == 0:
        list2 = c
        tup2 += tuple([list2])
if len(tup2) != 0:
    print(f'Os numeros pares foram: {tup2}')
else:
    print('Nao foram digitados numeros pares.')

