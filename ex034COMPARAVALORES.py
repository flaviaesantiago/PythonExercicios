n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segubdo numero: '))
if n1 > n2:
    print('O primeiro valor e maior pois {} e maior que {}.'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor e maior pois {} e maior que {}'. format(n2, n1))
else:
    print('Nao existe maior ou menor valor pois eles sao iguais.')
