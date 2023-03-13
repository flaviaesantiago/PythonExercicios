from random import randint


def sorteia(m):
    print('Sorteando 5 valores:')
    for c in range(5):
        m.append(randint(0, 10))
    for c in m:
        print(f'{c}',end=' ')


def somapar(n):
    s = 0
    print('\nSomando os valores pares:',end=' ')
    for x in n:
        if x % 2 == 0:
            s += x
    print(s)


li = []
sorteia(li)
somapar(li)