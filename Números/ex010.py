'''Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final. 
Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO", caso contrário, armazenar a nota da prova final e recalcular a média. 
Caso a nova média seja igual superior a 5, apresentar a mensagem "APROVADO", caso contrário, apresentar a mensagem "REPROVADO"'''


# receber as quatro notas do usuário e adicioná-las na lista
notas = []  
nota1 = float(input(f'Digite a primeira nota: '))
notas.append(nota1)
nota2 = float(input(f'Digite a primeira nota: '))
notas.append(nota2)
nota3 = float(input(f'Digite a primeira nota: '))
notas.append(nota3)
nota4 = float(input(f'Digite a primeira nota: '))
notas.append(nota4)

media = sum(notas) / len(notas)  # calcular a média das notas

if media >= 7:  # verificar se o aluno foi aprovado
    print("APROVADO")
else:
    print(f'Foi para prova final com a média:',(media))
    nota_final = float(input("Digite a nota da prova final: "))
    notas.append(nota_final) 
    nova_media = sum(notas) / len(notas) 
    if nova_media >= 5:
        print("APROVADO")
    else:
        print("REPROVADO")