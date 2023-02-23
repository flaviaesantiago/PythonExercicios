from datetime import date
atual = date.today().year
ano = int(input('Digite a seu ano de nascimento:'))
idade = atual - ano
if idade < 18:
    print('Voce tem {} anos, faltam {} anos para voce se alistar'.format(idade, (18 - idade)))
    print('Seu alistaemto sera em {}'.format((18 - idade) + atual))
elif idade == 18:
    print('Voce tem 18 anos, aliste-se IMEDIATAMENTE!.')
else:
    print('Voce tem {} anos. Voce devia ter se alistado a {} anos atras.'.format(idade, (idade - 18)))
    print('Seu alistaemto foi em {}'.format(atual - (idade - 18)))
