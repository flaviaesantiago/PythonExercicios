matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
som = col = ma = par = 0
for x in range(0, 3):
    for c in range(0, 3):
        matriz[x][c] = int(input(f'Digite um valor na posiçao [{x}][{c}]: '))
        som += matriz[x][c]
        col += matriz[x][2]
        if matriz[x][c] % 2 == 0:
            par += matriz[x][c]
for c in range(0, 3):
    if c == 0:
        ma = matriz[1][c]
    elif ma < matriz[1][c]:
        ma = matriz[1][c]
print('-=' * 30)
for x in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[x][c]:^5}]', end='')
    print()
print(f'A soma de todos os valores eh: {som}')
print(f' A soma dos valores pares: {par}')
print(f'A soma dos numeros da terceira coluna: {col}')
print(f'O maior numero da segunda linha: {ma} ')
