c = 0
x = 0
term2 = 1
soma = 10
term = int(input('Qual o primeiro termo da PA: '))
raz = int(input('Qual a razao da PA: '))
while c < 10:
    print(term, end=' . ')
    term += raz
    c += 1
print('PAUSA')
while term2 != 0:
    term2 = int(input('\nQuantos termos voce que mostrar a mais?'))
    if term2 != 0:
        soma += term2
        while x < term2:
            print(term, end=' . ')
            term += raz
            x += 1
        x = 0
        print('PAUSA.')
    else:
        print('FIM')
print('Foram mostrados {} termos.'.format(soma))
