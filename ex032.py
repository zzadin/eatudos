#ano bissexto
from datetime import date

# Solicita o ano ao usuário
ano = int(input('Que ano você quer analisar? Digite 0 para saber o ano atual: '))

# Se o usuário digitar 0, usa o ano atual
if ano == 0:
    ano = date.today().year

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano de {} é Bissexto!'.format(ano))
else:
    print('O ano de {} não é Bissexto!'.format(ano))