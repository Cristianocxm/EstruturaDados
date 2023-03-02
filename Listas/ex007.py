'''Criar uma lista com nomes de frutas e verificar se uma determinada fruta está na lista ou não.'''

frutas = ['limão', 'maça', 'pera', 'uva', 'carambola', 'laranja', 'melão', 'manga']

controle = True

for fruta in frutas:
    if fruta == 'melão':
        controle = False

if controle == False:
    print(f'Tem melão na lista.')

else:
    print(f'Não tem melão na lista.')