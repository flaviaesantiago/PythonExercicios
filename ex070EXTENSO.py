vint = ('zero', 'um', 'dois', 'tres',
        'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'quatorze', 'quinze', 'dezesseis', 'dezessete',
        'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um numero de zero a vinte:'))
    if n > 20:
        print('!ERRO!\nTente novamente. ', end='')
    else:
        print(f'Voce digitou o numero {vint[n]}')
        s = str(input('Deseja continuar? [S/N]').strip().upper()[0])
        if s == 'N':
            break