c = 0
term = int(input('Qual o primeiro termo da PA: '))
raz = int(input('Qual a razao da PA: '))
while c < 10:
    print(term, end=' . ')
    term += raz
    c += 1
print(' FIM ')
