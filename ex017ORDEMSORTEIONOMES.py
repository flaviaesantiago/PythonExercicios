from random import shuffle
print('Lista de alunos:')
nome1 = str(input('Aluno 1: '))
nome2 = str(input('Aluno 2: '))
nome3 = str(input('Aluno 3: '))
nome4 = str(input('Aluno 4: '))
sort = [nome1, nome2, nome3, nome4]
shuffle(sort)
print('A ordem de apresentacao sera: {}'.format(sort))
