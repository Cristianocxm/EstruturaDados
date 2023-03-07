'''Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a média final, a maior nota e a menor nota'''

notas = []

nota1 = float (input(f'informe a 1º nota: '))
notas.append(nota1)
nota2 = float (input(f'informe a 2º nota: '))
notas.append(nota2)
nota3 = float (input(f'informe a 3º nota: '))
notas.append(nota3)
nota4 = float (input(f'informe a 4º nota: '))
notas.append(nota4)


media = sum(notas) / len(notas)


maior_nota = max(notas)


menor_nota = min(notas)


print(f"Média final: {media:.2f}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")