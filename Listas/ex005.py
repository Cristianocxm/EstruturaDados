'''Criar uma lista com números inteiros e contar quantos números pares e quantos números ímpares existem na lista.'''

inteiros = [2, 5, 6, 12, 15, 19, 23, 25, 29, 45, 47, 48, 58, 63, 68, 74, 86, 93, 94, 1000, 1002]

pares = 0

impares = 0

for n in inteiros:

    if n%2 == 0:
        pares += 1
    
    else:
        impares += 1

print('Total de números pares: ', pares)

print('Total de números ímpares: ', impares)