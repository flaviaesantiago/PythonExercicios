sal = float(input('Valor do salario: '))
if sal > 1250.00:
    nsal = sal + (sal * 0.10)
else:
    nsal = sal + (sal * 0.15)
print('O novo salario sera de: R${:.2f}'.format(nsal))
