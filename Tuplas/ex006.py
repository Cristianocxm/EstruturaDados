'''Criar uma tupla com números inteiros e verificar se um determinado número está na
tupla ou não.'''

inteiros = (2, 5, 6, 12, 15, 19, 23, 25, 29, 45, 47, 48, 58, 63, 68, 74, 86, 93, 94, 1000, 1002)

controle = True

numero = int(input('Digite o número que deseja verificar se está na listagem: '))

for valor in inteiros:
    if valor == numero:
        controle = False


if controle == False:
    print(f'O número {numero} está na lista.')

else:
    print(f'O número {numero} não está na lista.')