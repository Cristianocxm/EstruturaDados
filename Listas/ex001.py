'''Criar uma lista com 10 números inteiros aleatórios e imprimir o maior e o menor número da lista.'''

inteiros = [98, 15, 2, 58, 1, 1002, 48, 98, 47, 1000000, 7]

length = 0

for i in inteiros:
    length += 1

for i in range(length):
    for j in range(i+1,length):
        aux = inteiros[i]
        if inteiros[i] > inteiros[j]:
            inteiros[i] = inteiros[j]
            inteiros[j] = aux

print(f'O maior número é {inteiros[0]}.')
print(f'O menor número é {inteiros[length-1]}.')


