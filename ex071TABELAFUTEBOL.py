times = ('Palmeiras', 'Corinthians', 'Fluminense',
         'Flamengo', 'Atletico', 'Internacional',
         'Bragantino', 'Santos', 'Sao Paulo', 'Goias')
print('= = =' * 30)
print('Os 5 primeiros colocados sao:', times[0:5])
print('= = =' * 30)
print('os 4 ultimos colocados sao: ', times[-4:])
print('= = =' * 30)
print('Times em ordem alfabetica: ', sorted(times))
print('= = =' * 30)
print('Santos esta em ', times.index('Santos')+1, 'º lugar.')
