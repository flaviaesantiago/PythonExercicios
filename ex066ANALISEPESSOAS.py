idade = qh = qm = m = 0
sexo = cont = ''
while True:
    sexo = str(input('Qual o seu sexo? [M/F]: ')).strip().upper()[0]
    idade = int(input('Qual a sua idade? '))
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        m += 1
    if sexo == 'M':
        qh += 1
    elif idade < 20:
        qm += 1
    if cont == 'N':
       break
print('= = = = = = = = = ' * 5)
print(f'''PESSOAS MAIORES DE IDADE: {m} 
HOMENS CADASTRADOS: {qh} 
MULHERES COM MENOS DE 20 ANOS: {qm}''')
