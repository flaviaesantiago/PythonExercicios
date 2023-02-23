n1 = float(input('Preço do produto:'))
n = int(input('Desconto:'))
d = (n*0.01)
print('Com desconto de {}%, o novo preço sera de: {}'.format(n, n1 - (n1*d)))
