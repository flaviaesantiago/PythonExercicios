numero = int(input('Escreva um numero: '))
print('- - - - ' * 5)
print('M E N U  D E  E S C O L H A:')
print('- - - - ' * 5)
print('[1] Binario')
print('[2] Octal')
print('[3] Hexadecimal')
print('- - - - ' * 5)
menu = int(input('Escolha uma opcao do menu: '))
if menu == 1:
    print('{} em binario: {}'.format(numero, bin(numero)[2:]))
elif menu == 2:
    print('{} em Octal: {}.'.format(numero, oct(numero)[2:]))
elif menu == 3:
    print('{} em Hexadecimal: {}'.format(numero, hex(numero)[2:]))
else:
    print('Opcao invalida. Operaçao terminada')
