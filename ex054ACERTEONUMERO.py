rodadas = 0
from time import sleep
from random import randrange
ale = randrange(10)
pitaco = int(input('Em qual numero estou pensando?'))
print('PROCESSANDO...')
sleep(1)
while pitaco != ale:
    while pitaco < ale:
        pitaco = int(input('Mais... Tente novamente:'))
        rodadas += 1
        print('PROCESSANDO...')
        sleep(1)
    while pitaco > ale:
        pitaco = int(input('Menos... Tente novamente:'))
        rodadas += 1
        print('PROCESSANDO...')
        sleep(1)
if pitaco == ale:
    print('PARABENS! VOCE ACERTOU na {}ª rodada!'.format(rodadas+1))
