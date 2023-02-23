matriz = []
tot = par = 0
for c in range(0, 3):
    for x in range(0, 3):
        n = int(input(f'Digite um valor para [{c}, {x}]: '))
        matriz.append(n)
        tot += n
x = 0
for c in range(0, 3):
    print(f'[ {matriz[x]:^5} ][ {matriz[x+1]:^5} ][ {matriz[x+2]:^5} ]')
    x += 3
for c in range(len(matriz)):
    if matriz[c] % 2 == 0:
        par += matriz[c]
print(f'A soma de todos os valores e: {tot}')
print(f'A soma dos valores pares: {par} ')
print(f'A soma dos valores da terceira coluna e: {matriz[2] + matriz[5] + matriz[8]}')
ma = matriz[3]
if ma < matriz[5] > matriz[4]:
    ma = matriz[5]
elif ma < matriz[4] > matriz[5]:
    ma = matriz[4]
print(f'O maior valor da segunda linha e: {ma}')
