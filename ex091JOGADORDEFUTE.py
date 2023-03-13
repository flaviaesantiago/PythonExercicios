dados = {}
part = []
dados['nome'] = str(input('Nome do jogador: '))
t = int(input(f'Quantas partidas {dados["nome"].capitalize()} jogou: '))
for p in range(0, t):
    part.append(int(input(f'Gols marcados na {p+1}ª partida: ')))
    dados['gols'] = part[:]
    dados["total"] = sum(part)
print('=-' * 20)
for k, v in dados.items():
    print(f'o campo {k} tem valor {v}')
print('=-' * 20)
print(f'{dados["nome"].capitalize()} jogou {t} partidas.')
for p in range(0, len(dados["gols"])):
    print(f'No {p + 1}º jogo, marcou {part[p]} gols')
# OU for i, v in enumerate(dados["gols"]
    #print(f'   Na partida {i}, marcou {v} gols.)
print(f'{dados["nome"].capitalize()} marcou um total de {dados["total"]} gols')
print('=-' * 20)
print(dados)