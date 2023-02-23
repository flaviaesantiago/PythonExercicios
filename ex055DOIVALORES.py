from time import sleep
m = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
menu = 0
while menu != 5:
    menu = int(input('---- MENU ----\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NUMEROS\n[5]SAIR\n------------\nOpçao: '))
    if menu == 1:
        print('A soma entre {}+{}={}'.format(n1, n2, (n1+n2)))
    elif menu == 2:
        print('{} multiplicado por {} = {}'.format(n1, n2, (n1*n2)))
    elif menu == 3:
        if n1 > n2:
            m = n2
        elif n2 > n1:
            m = n2
        print('Entre {} e {} o maior valor eh {}.'.format(n1, n2, m))
        if n1 == n2:
            print('Ambos tem valor {}'.format(n1))
    elif menu == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif menu != 5:
        print('OPÇAO INVALIDA. Tente novamente.')
    sleep(1)
print('VOCE SAIU DO ANALISADOR DE NUMEROS')