p = float(input('Preço do produto: '))
print('{:=^40}'.format(' OPCOES DE PAGAMENTO '))
print(' ' * 5)
print('''[1] Dinheiro/Cheque
[2] Cartao''')
print('- - - -' * 5)
m = int(input('Opcao de pagamento:'))
if m == 1:
    p = p - (p * 0.10)
    print('O novo preço com 10% de desconto sera de: R${:.2f}'.format(p))
elif m == 2:
    print('- - - -' * 5)
    print('''MENU CARTAO:
    [1] A vista:
    [2] 2x no cartao
    [3] De 3X ate 10x no cartao''')
    print('- - - -' * 5)
    c = int(input('Opçao de cartao: '))
    if c == 1:
        p = p - (p * 0.05)
        print('O novo preço com 5% de desconto sera de: R${:.2f}'.format(p))
    elif c == 2:
        print('O preço sera de R${:.2f} em duas parcelas de R${:.2f}'.format(p, (p/2)))
    elif c == 3:
        par = int(input('Quantas parcelas deseja:'))
        p = p + (p * 0.20)
        print('O novo preço com 20% de juros sera de: R${:.2f}. Em {} parcelas de R${:.2f}'.format(p, par, (p/par)))
