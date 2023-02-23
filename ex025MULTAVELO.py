velo = int(input('Quantos km/h o carro estava?'))
multa = 7 * (velo - 80)
print('Velocidade permitida.' if velo <= 80.0 else '{}km/h acima do limite. Sua multa e de R${:.2f}'.format((velo - 80), multa))

