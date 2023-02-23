c = 1
qu = 10
total = 0
term = int(input('Qual o primeiro termo da PA: '))
raz = int(input('Qual a razao da PA: '))
while qu != 0:
    total += qu
    while c < total:
        print(term, end=' . ')
        term += raz
        c += 1
    print('PAUSA')
    qu = int(input('Quantos termos voce que mostrar a mais?'))
print(' FIM. {} termos mostrados '.format(total))
