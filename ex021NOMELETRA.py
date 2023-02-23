nome = str(input('Digite uma frase: ')).strip().upper()
print('Sua frase tem {} letras A.'.format(nome.count('A')))
print('A primeira apariçao de A eh na posiçao: {}.'.format(nome.find('A')+1))
print('A ultima apariçao de A eh na posiçao: {}.'.format(nome.rfind('A')+1))
