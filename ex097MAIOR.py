def maior(*n):
    print('-='*20)
    print('Analisando os numeros...')
    for c in n:
        print(f'{c}',end=' ')
    if 0 in n and len(n) == 1:
        print(f'\nNenhum numero foi informado.')
    else:
        print(f'\nQuantos numeros informados: {len(n)}. \nO maior numero foi: {sorted(n)[-1]}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
