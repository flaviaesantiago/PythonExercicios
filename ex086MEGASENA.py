from random import randrange
import time
jogo = []
n = int(input('Quantos palpites de jogos voce deseja gerar? '))
print(f'-=-=-= SORTEANDO {n} JOGOS -=-=-=-=')
for c in range(0, n):
    for x in range(0, 6):
        jogo.append(randrange(1, 60))
    time.sleep(1)
    print(f'JOGO {c+1}: {sorted(jogo)}')
    jogo.clear()
print(f'<<<<<<<<<<<< BOA SORTE! >>>>>>>>>>>>')
