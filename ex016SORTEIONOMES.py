from random import choice
print('Lista de alunos: ')
nome1 = str(input('Aluno 1: '))
nome2 = str(input('Aluno 2: '))
nome3 = str(input('Aluno 3: '))
sort = choice([nome1, nome2, nome3])
print('Resultdo do sorteio:')
print('O aluno sorteado foi {}.'.format(sort))
