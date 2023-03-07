'''Considere o seguinte dicionário: {'m1': {'m2': 'Olá Mundo'}}. Carregue e apresente a mensagem "Olá Mundo" contida no dicionário'''

dicionario = {'m1': {'m2': 'Olá Mundo'}}

valor = dicionario.get('m1').get('m2')

print(valor)