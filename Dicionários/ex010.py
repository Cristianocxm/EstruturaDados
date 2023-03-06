'''Armazenar uma contagem de palavras em um texto usando um dicionário, onde
as palavras são os atributos e as contagens são os valores'''

texto = 'Armazenar uma contagem de palavras em um texto usando um dicionário, onde as palavras são os atributos e as contagens são os valores'

texto = texto.lower()

palavras = texto.split(' ')

contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] = contagem[palavra] + 1
    else:
        contagem[palavra] = 1

for chave, valor in contagem.items():
    print(f'{chave}: {valor} ocorrência(s)')
    