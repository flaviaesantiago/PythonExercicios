s = qu = n = 0
while n != 999:
    n = int(input('Digite um valor: (999 para sair)'))
    if n != 999:
        s += n
        qu += 1
print('Voce digitou {} numeros e a soma entre eles foi de {}'.format(qu, s))
