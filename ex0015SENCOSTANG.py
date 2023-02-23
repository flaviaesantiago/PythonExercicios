from math import radians, cos, sin, tan
ang = float(input('Digite a medida de um angulo: '))
rad = radians(ang)
print('O conseno desse angulo eh: {:.2f}. O seno desse angulo eh: {:.2f}.'.format(cos(rad), sin(rad)))
print('A tangente desse angulo eh: {:.2f}'.format(tan(rad)))
