palavras = ()
p = int(input('Quantas palavras voce quer cadastrar?: '))
for c in range(0, p):
    pal = str(input('Escreva uma palavra: '))
    palavras += tuple([pal])
for pala in palavras:
    print(f'\nNa palavra {pala} temos ', end='')
    for letra in pala:
        if letra.upper() in 'AEIOU':
            print(letra, end=', ')
