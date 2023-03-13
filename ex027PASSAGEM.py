ds = int(input('Qual a distancia em km?'))
p = ds * 0.50 if ds <= 200 else ds * 0.45
print('A passagem custara: R${:.2f}'.format(p))
