vs = []
while True:
    vs.append(int(input('Digite um valor:')))
    sn = str(input('Deseja continuar?')).strip().upper()[0]
    if sn in 'N':
        break
print(f'Voce digitou {len(vs)} valores')
vs.sort(reverse=True)
print(f'Os valores em ordem descrescente foram: {vs}')
if 5 in vs:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 nao faz parte da lista.')