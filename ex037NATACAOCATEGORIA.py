from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print('- - - -' * 5)
print('{} anos.'.format(idade))
if idade <= 9:
    print('CATEGORIA: MIRIM')
elif 14 >= idade:
    print('CATEGORIA: INFANTIL')
elif 19 >= idade:
    print('CATEGORIA: JUNIOR')
elif 25 >= idade:
    print('CATEGORIA: SENIOR')
else:
    print('CATEGORIA MASTER')
print('- - - -' * 5)
