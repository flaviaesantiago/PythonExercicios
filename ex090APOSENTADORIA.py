from datetime import date
dados = {}
dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
dados['ano'] = date.today().year - ano
dados['cart'] = int(input('Numero da carteira de trabalho: '))
if dados["cart"] != 0:
    dados['cont'] = int(input('Ano de contrataçao?:  '))
    dados['sal'] = float(input('Salario R$: '))
    print('-=' * 20)
    dados["fut"] = date.today().year - dados["cont"]
    dados["fut"] = 35 - dados["fut"]
    if dados["fut"] > 0:
        print(f'{dados["nome"].capitalize()} de {dados["ano"]} anos,'
              f' com {date.today().year - dados["cont"]} anos de contribuiçao,'
              f' podera se aposentar no ano de {date.today().year + dados["fut"]} '
              f'com {dados["ano"]+dados["fut"]} anos.')
    else:
        print(f'{dados["nome"].capitalize()} ja pode se aposentar desde {dados["cont"]+35}.')
else:
    print(f'{dados["nome"].capitalize()} de {dados["ano"]} anos nao tem carteira de trabalho.')
