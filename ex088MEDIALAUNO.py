situ = {"nome": str(input('Nome: '))}
situ["media"] = float(input(f'Media de {situ["nome"].capitalize()}: '))
if situ["media"] < 6:
    situ['situaçao'] = 'Reprovado'
elif 5 <= situ["media"] <= 7:
    situ['situaçao'] = 'Em recuperaçao'
elif situ["media"] > 7:
    situ['situaçao'] = 'Aprovado'
print(f'Nome: {situ["nome"]}\nMedia: {situ["media"]}\nSituaçao: {situ["situaçao"]}')
