vs = []
while True:
    v = int(input('Digite um valor: '))
    if v not in vs:
        vs.append(v)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor repetido, tente novamente.')
    sn = str(input('Deseja continuar?').strip().upper()[0])
    print('-=' * 30)
    if sn == 'n':
        break
print(f'Os valores nao repetidos em ordem crescente foram: {sorted(vs)}')
