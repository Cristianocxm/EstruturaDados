'''Criar uma lista com nomes de pessoas e ordená-la alfabeticamente.'''

nomes = ['Osvaldo','Maria','Joaquim','Robson','Cremildo','Josué','Américo']

length = 0

for i in nomes:
    length += 1

for i in range(length):
    for j in range(i+1,length):
        aux = nomes[i]
        if nomes[i] > nomes[j]:
            nomes[i] = nomes[j]
            nomes[j] = aux

print(nomes)