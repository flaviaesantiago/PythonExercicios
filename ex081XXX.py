ex = str(input('Digete uma expressao: '))
pilha = []
for sim in ex:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao e valida')
else:
    print('Sua expressao nao e valida. confira os parentesis.')
