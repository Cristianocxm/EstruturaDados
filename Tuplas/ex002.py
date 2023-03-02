'''Criar duas tuplas de números inteiros e mesclá-las em uma terceira tupla em ordem
crescente.'''

tupla1 = (5, 15, 2, 58, 1000, 1002, 48, 63, 47, 94)

tupla2 = (6, 12, 68, 45, 74, 19, 86, 23, 25, 29, 93)

tupla3 = tupla1 + tupla2

lista1 = []

length = 0

for i in tupla3:
    length += 1
    lista1.append(i)

for i in range(length):
    for j in range(i+1,length):
        aux = lista1[i]
        if lista1[i] > lista1[j]:
            lista1[i] = lista1[j]
            lista1[j] = aux

tupla = tuple(lista1)

print(type(tupla))
print(tupla)