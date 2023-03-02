'''Remover todas as ocorrências de um determinado número de uma tupla de números
inteiros.'''

tupla = (5, 15, 2, 58, 1000, 1002, 5, 48, 63, 47, 5, 94)

numeros = []

for i in tupla:
    numeros.append(i)

soma = 0

for n in numeros:
    if n == 5:
        numeros.remove(n)
        soma += 1

tupla = (tuple(numeros))

print(f'Foram encontradas e removidas {soma} ocorrências do número 5. A nova tupla é: ')

print(tupla)