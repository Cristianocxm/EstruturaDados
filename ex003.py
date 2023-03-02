'''Criar uma tupla com nomes de pessoas e ordená-la alfabeticamente'''

nomes = ('Osvaldo','Maria','Joaquim','Robson','Cremildo','Josué','Américo')

lista_Nomes = []

length = 0

for i in nomes:
    length += 1
    lista_Nomes.append(i)

for i in range(length):
    for j in range(i+1,length):
        aux = lista_Nomes[i]
        if lista_Nomes[i] > lista_Nomes[j]:
            lista_Nomes[i] = lista_Nomes[j]
            lista_Nomes[j] = aux


print(type(tuple(lista_Nomes)))
print(tuple(lista_Nomes))

