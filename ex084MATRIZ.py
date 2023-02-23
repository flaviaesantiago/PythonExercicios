matriz = []
sp = st = ma = 0
for c in range(0, 3):
    for x in range(0, 3):
        n = int(input(f'Digite um valor para [{c}, {x}]: '))
        matriz.append(n)
x = 0
for c in range(0, 3):
        print(f'[{matriz[x]:^5}][{matriz[x+1]:^5}][{matriz[x+2]:^5}]')
        x += 3
for i in range(len(matriz)):
    if matriz[i] % 2 == 0:
            sp += matriz[c]
print(f'A soma de todos os velores e: {sum(matriz)}')
print(f'A soma dos valores pares: {sp}')
print(f'A soma dos valores da trceira coluna e:{matriz[2] + matriz[5] + matriz[8]}')
ma = matriz[3]
if ma < matriz[4] > matriz[5]:
    ma = matriz[4]
elif ma < matriz[5] > matriz[4]:
    ma = matriz[5]
print(f'O maior valor da linha 2 e: {ma}')
