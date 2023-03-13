from time import sleep


def area(la, co):
    print(f'Area total: {la*co}m²')


def lin(msg):
    print('=-'*20)
    print(f'{msg:^38}')
    print('=-'*20)


lin('CALCULADORA DE AREA')
l = float(input('Largura do terreno (m):'))
c = float(input('Comprimento da area (m): '))
lin('CALCULANDO...')
sleep(1)
area(l, c)