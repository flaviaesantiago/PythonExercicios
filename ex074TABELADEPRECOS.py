c = int(input('Quantos produtos deseja cadastrar?'))
preco = 0
produto = ''
tup = ()
for x in range(c):
    produto = str(input(f'Produto {x+1}:'))
    preco = float(input(f'Preço: '))
    tup += tuple([produto,preco])
for x in range(len(tup)):
    if x % 2 == 0:
        print(f'{tup[x]:.<15}'.capitalize(), end='')
    else:
        print(f' R${tup[x]:>7.2f}')

