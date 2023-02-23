from random import randrange
list = [randrange(10) for c in range(0, 5)]
print(f'Os numeros sorteados foram: {list}')
a = sorted(list)
print(f'O menor valor foi: {a[0]}\nO maior valor foi:{a[-1]}')

