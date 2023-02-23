num = []
num.append(str(input('Digite uma expressao: ')))
num.count('(') == num.count(')')
for c in range(0, len(num)):
    if '(' in len(num[c]):
        if ')' in len(num[-c]):
            print('Sua expressao esta correta.')
