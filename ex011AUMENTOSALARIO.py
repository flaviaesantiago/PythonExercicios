p = float(input('Qual o salario atual?'))
a = int(input('Porcentagem do reajuste: '))
po = a * 0.01
print('Com o reajuste de {}%, o novo salario sera de {:.2f} .'.format(a, p + (p * po)))
