'''Desenvolva um programa que leia quatro notas e que apresente a média final'''

ordem = ['primeira','segunda','terceira','quarta']



soma = 0

contador = 0

for i in ordem:
    nota = float(input(f'Digite sua {i} nota: '))
    soma += nota
    contador += 1

media = soma/contador

print(f'A média é: {media}')
