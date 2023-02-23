from math import sqrt, pow
num = int(input('Comprimento do cateto oposto: '))
num2 = int(input('Comprimento do cateto adjacente: '))
cat = pow(num, 2) + pow(num2, 2)
hip = sqrt(cat)
print(' cateto 1 {} \n e cateto 2 {}.\n O comprimento da hipotenusa eh: {:.2f}'.format(sqrt(num), sqrt(num2), hip))
