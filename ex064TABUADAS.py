from time import sleep
print('= = = = T A B U A D A = = = = =')
while True:
    sleep(1)
    print('-------------------')
    n = int(input('Quero ver a tabuada de: '))
    print('-------------------')
    if n == 0:
        break
    print(f' ----- Tabuada de {n} -----')
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
