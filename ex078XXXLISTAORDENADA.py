vs = []
q = int(input('Quantos valores deseja adicionar? '))
for c in range(q):
    v = int(input('Digite um valor:'))
    if c == 0 or v > vs[-1]:
        vs.append(v)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(vs):
            if v <= vs[pos]:
                vs.insert(pos, v)
                print(f'Adicionado na posiçao {pos}')
                break
            pos += 1
print(f'Os valors digitados em ordem crescente foram {vs}')
