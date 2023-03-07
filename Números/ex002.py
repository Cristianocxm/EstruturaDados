'''Carregue a data atual do computador e apresente somente a data'''

import datetime

data = datetime.date.today().strftime('%d/%m/%Y')

print(f'A data é: {data}')