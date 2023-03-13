from random import randrange
from time import sleep
from operator import itemgetter
print(f'Valores sorteados:')
jogo = {'Jogador 1' : randrange(1,6),
        'Jogador 2' : randrange(1,6),
        'Jogador 3' : randrange(1,6),
        'Jogador 4' : randrange(1,6)}
for c, v in jogo.items():
    sleep(.5)
    print(f' {c} tirou {v}.')
print('=-=-=-='*3)
print(f'{"RANKING":=^20}')
ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True)
for c, v in enumerate(ranking):
    print(f'Em {c+1}º {v[0]} com {v[1]} pontos.')
