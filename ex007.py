'''Criar uma tupla com nomes de frutas e verificar se uma determinada fruta está na
tupla ou não'''

frutas = ('limão', 'maça', 'pera', 'uva', 'carambola', 'laranja', 'melão', 'manga')

controle = True

fruta = input('Digite a fruta: ')

for f in frutas:
    if f == fruta:
        controle = False

if controle == False:
    print(f'Tem {fruta} na lista.')

else:
    print(f'Não tem {fruta} na lista.')
