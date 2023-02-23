term = int(input('Qual o primeiro termo da PA: '))
raz = int(input('Qual a razao da PA: '))
for c in range(1, 11):
    print(term, end=' . ')
    term += raz
