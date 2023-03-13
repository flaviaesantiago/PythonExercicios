def maior(n):
    print('-='*20)
    print('Analisando os numeros...')
    for c in n:
        print(f'{c}', end=' ')
    if 0 in n and len(n) == 1:
        print(f'\nNenhum numero foi informado.')
    else:
        print(f'\nQuantos numeros informados: {len(n)}. \nO maior numero foi: {sorted(n)[-1]}')


li = []
while True:
    r = int(input('Quantos valores gostaria de digitar?'))
    for x in range(r):
        v = int(input(f'{x+1}º valor:'))
        li.append(v)
    maior(li)
    li.clear()
    s = str(input('Deseja digitar novos numeros?')).strip().upper()[0]
    if s in 'N':
        print('ENCERRADO')
        break