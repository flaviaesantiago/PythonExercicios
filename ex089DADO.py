from random import randint
from time import sleep
from operator import itemgetter
resultados = {'Jogador1' : randint(1, 6),
              'Jogador2' : randint(1, 6),
              'Jogador3' : randint(1, 6),
              'Jogador4' : randint(1, 6)}
ordem = []
print('valores sorteados:')
for k, v in resultados.items():
    print(f'{k} tirou {v}. ')
    sleep(1)
ordem = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print(f'{"RANKING":=^40}')
for i, v in enumerate(ordem):
    sleep(1)
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')