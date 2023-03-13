from time import sleep


def cont(i, f, p):
    if f > i or p < 0:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.5)
    else:
        for c in range(i, f-1, -p):
            print(c, end=' ')
            sleep(0.5)


while True:
    ii = int(input('Inicio: '))
    ff = int(input('Fim: '))
    pp = int(input('Intervalo: '))
    cont(ii, ff, pp)
    r = str(input('FIM!\nDeseja continuar? [S/N]')).strip().upper()
    if 'N' in r:
        break
print('ENCERRADO')
