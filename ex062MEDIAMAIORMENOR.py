m = ma = s = q = me = 0
p = 'S'
while p in 'Ss':
    n = int(input('Digite um valor'))
    p = str(input('Deseja continuar? [SIM] / [NAO]: ')).upper().strip()[0]
    s += n
    q += 1
    m = s/q
    if q == 1:
        ma = me = n
    else:
        if n > m:
            ma = n
        if n < me:
            me = n
print(' Voce digitou {} valores, a media entre os numeros: {}. Maior valor: {}. Menor valor: {}'.format(q, m, ma, me))
