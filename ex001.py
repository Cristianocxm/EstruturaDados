'''Criar uma tupla com 10 números inteiros aleatórios e imprimir o maior e o menor
número da tupla.'''

inteiros = (98, 15, 2, 58, 1, 1002, 48, 98, 47, 1000000, 7)

lista_Inteiros = []

length = 0

for i in inteiros:
    length += 1
    lista_Inteiros.append(i)

for i in range(length):
    for j in range(i+1,length):
        aux = lista_Inteiros[i]
        if lista_Inteiros[i] > lista_Inteiros[j]:
            lista_Inteiros[i] = lista_Inteiros[j]
            lista_Inteiros[j] = aux

tupla = tuple(lista_Inteiros)

print(f'O maior número é {tupla[0]}.')
print(f'O menor número é {tupla[length-1]}.')