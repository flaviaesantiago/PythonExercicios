casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual e o salario atual?'))
anos = int(input('Em quantos anos pretende quitar a casa?'))
par = casa / (anos * 12)
por = par / (sal / 100)
print('A parcela sera de: R${:.2f}'.format(par))
if par < (sal * 0.30):
    print('isso sera {:.1f}% do seu salario. Voce podera pegar um emprestimo!'.format(por))
else:
    print('Infelizmente, isso seria {:.1f}% do seu salario e excede o limite de 30%. Nao podemos autorizar.'.format(por, par))
