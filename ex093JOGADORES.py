from time import sleep
dados = {}
lista = []
part = []
while True:
    dados['nome'] = str(input('Nome do jogador: '))
    t = int(input(f'Quantas partidas {dados["nome"].capitalize()} jogou: '))
    for p in range(0, t):
        part.append(int(input(f'Gols marcados na {p+1}ª partida: ')))
        dados['gols'] = part[:]
        dados["total"] = sum(part)
    part.clear()
    lista.append(dados.copy())
    r = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    print('-=' * 20)
    if r == 'N':
        break
for k, v in dados.items():
    print(f'o campo {k} tem valor {v}')
print('=-' * 20)
print(f'{dados["nome"].capitalize()} jogou {len(dados["gols"])} partidas.')
for i, v in enumerate(dados["gols"]):
    print(f'   Na partida {i}, marcou {v} gols.')
print(f'{dados["nome"].capitalize()} marcou um total de {dados["total"]} gols')
print('=-' * 20)
print(f'{"cod":<5}{"NOME":<12}{"GOLS":<15}{"TOTAL":<5}')
for p in range(0, len(lista)):
    print(f'{p+1:<5}{lista[p]["nome"].capitalize():<12}{lista[p]["gols"]}{lista[p]["total"]:<5}')
while True:
    print('-=' * 20)
    n = int(input('mostrar dados de qual jogador?'))
    if 0 < n < len(lista)+1:
        print(f'LEVANTAMENTO DO JOGADOR {lista[n - 1]["nome"].capitalize()}')
        for k in range(0, len(lista[n - 1]["gols"])):
            print(f'No jogo {k + 1} fez {lista[n - 1]["gols"][k]} gols.')
        print(f'Total de {lista[n-1]["total"]} gols.')
    elif n > len(lista)+1:
        print('Esse jogador nao existe. Tente novamente')
    if n == 0:
        break
print('FINALIZANDO...')
sleep(1)
print(' >>>>> VOLTE SEMPRE <<<<<.')