nome = str(input('Nome completo: ')).strip()
nome = nome.split()
print('Primeiro nome: {}.'.format(nome[0].capitalize()))
print('Ultimo nome: {}.'.format(nome[len(nome)-1].capitalize()))
