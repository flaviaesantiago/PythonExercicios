f = str(input('Escreva uma frase')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
print('{} invertido eh {}'.format(junto, junto[::-1]))
if junto == junto[::-1]:
    print('\"{}\" eh um palindromo'.format(f.capitalize()))
else:
    print('\"{}\" nao eh um palindromo'.format(f.capitalize()))
