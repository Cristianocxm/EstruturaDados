'''Criar uma lista com números inteiros e verificar se um determinado número está na lista ou não.'''

inteiros = [2, 5, 6, 12, 15, 19, 23, 25, 29, 45, 47, 48, 58, 63, 68, 74, 86, 93, 94, 1000, 1002]

controle = True

for valor in inteiros:
    if valor == 6:
        controle = False


if controle == False:
    print('O número 6 está na lista.')

else:
    print('O número 6 não está na lista.')