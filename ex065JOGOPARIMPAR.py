from random import randrange
eu = ''
j = 1
g = 0
while j != 0:
    comp = randrange(10)
    eu = str(input('PAR OU IMPAR?'))
    eu2 = int(input('Escolha um  numero: '))
    soma = comp + eu2
    if eu == 'par' and soma % 2 == 0 or eu == 'impar' and soma % 2 == 1:
        print(f'Voce escolheu {eu}. Eu escolhi {comp}, voce escolheu {eu2}. Deu {soma}! VOCE GANHOU!')
        g += 1
    else:
        print(f'Voce escolheu {eu}.Eu escolhi {comp} e voce escolheu {eu2}.Deu {soma}! VOCE PERDEU!')
        j = 0
print(f'Voce ganhou {g} partidas.')
