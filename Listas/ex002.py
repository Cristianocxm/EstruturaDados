'''Criar duas listas de números inteiros e mesclá-las em uma terceira lista em ordem crescente.'''

lista1 = [5, 15, 2, 58, 1000, 1002, 48, 63, 47, 94]

lista2 = [6, 12, 68, 45, 74, 19, 86, 23, 25, 29, 93]

lista3 = lista1 + lista2

length = 0

for i in lista3:
    length += 1

for i in range(length):
    for j in range(i+1,length):
        aux = lista3[i]
        if lista3[i] > lista3[j]:
            lista3[i] = lista3[j]
            lista3[j] = aux

print(lista3)