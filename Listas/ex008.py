'''Criar uma lista de números inteiros e calcular a soma de todos os números na lista.'''

inteiros = [2, 5, 6, 12, 15, 19, 23, 25, 29, 45, 47, 48, 58, 63, 68, 74, 86, 93, 94, 1000, 1002]

soma = 0

for n in inteiros:
    soma += n

print('A soma total é: ', soma)