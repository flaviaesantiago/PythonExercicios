situ = {}
situ["nome"] = str(input('Nome: '))
situ["media"] = float(input(f'Media de {situ["nome"].capitalize()}: '))
if situ["media"] < 6:
    situ['situaçao'] = 'Reprovado'
elif situ["media"] >= 5 and situ["media"] <= 7:
    situ['situaçao'] = 'Em recuperaçao'
elif situ["media"] > 7:
    situ['situaçao'] = 'Aprovado'
print(f'O nome eh {situ["nome"]}\nA media eh {situ["media"]}\nA situacao eh {situ["situaçao"]}')
