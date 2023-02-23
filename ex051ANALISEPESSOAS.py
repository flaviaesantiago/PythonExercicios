from datetime import date
hj = date.today().year
soma = 0
mulheres = 0
for c in range(1, 5):
    pessoa = str(input('-----{}º PESSOA-----'.format(c)))
    ano = int(input('Ano nascimento: '))
    mf = str(input('Sexo (M ou F): '))
    i = hj - ano
    soma += i
    if c == 1:
        maior = i
    if mf == 'f' and i < 20:
        mulheres += 1
    elif mf == 'm':
        if maior < i:
            maior = i
            homi = pessoa
print('A media de idade do grupo eh de: {:.1f}'.format(soma/4))
print('O nome do homem mais velho eh {} com {} anos.'.format(homi, maior))
print('Existem {} mulheres com menos de 20 anos.'.format(mulheres))
