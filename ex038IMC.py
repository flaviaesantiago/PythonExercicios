peso = float(input('Seu peso em kg:'))
altura = float(input('Sua altura em metros: '))
imc = peso / (altura**2)
print('- - - ' * 5)
print('IMC : {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc <= 25:
    print('PESO IDEAL')
elif imc <= 30:
    print('SOBREPESO')
elif imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')
print('- - - -' * 5)
