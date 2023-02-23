nome = ''
s = caro = q = barato = 0
while True:
    pro = str(input(' Item comprado: ')).strip()
    pre = float(input('Preço: '))
    usu = str(input(' Deseja continuar? [S/N]: ')).strip().upper()
    s += pre
    q += 1
    if q == 1 or pre < barato:
        barato = pre
        nome = pro
    if pre > 1000.00:
        caro += 1
    if usu == 'N':
        break
print(f'''TOTAL DA COMPRA: R${s:.2f}
PRODUTOS QUE CUSTAM MAIS DE MIL REAIS: {caro} ITENS
PRODUTO MAIS BARATO: {nome.capitalize()}: R$: {barato:.2f}''')
