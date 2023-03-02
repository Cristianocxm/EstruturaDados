'''Remover todas as ocorrências de um determinado número de uma lista de números inteiros.'''

inteiros = [5, 15, 2, 58, 1000, 1002, 5, 48, 63, 47, 5, 94]

soma = 0

for n in inteiros:
    if n == 5:
        inteiros.remove(n)
        soma += 1
print(f'Foram encontradas e removidas {soma} ocorrências do número 5. A nova lista é: ')

print(inteiros)