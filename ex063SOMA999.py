s = q = 0
while True:
    n = int(input('Digite um numero: (999 para interromper) '))
    if n == 999:
        break
    s += n
    q += 1
print(f' A soma entre os {q} numeros digitados foi: {s}.')
