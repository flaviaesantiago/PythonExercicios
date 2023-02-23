from random import randrange
from time import sleep
n2 = randrange(5)
n1 = int(input('De 0 a 5, em qual numero estou pensando?'))
print('PROCESSANDO...')
sleep(1)
print('{}! Parabens! Voce acertou!'.format(n2) if n1 == n2 else 'Voce errou, o numero que eu estava pensando era {}'.format(n2))
