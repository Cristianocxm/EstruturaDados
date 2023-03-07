'''Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar'''

def verificaNumero(x):
    if x%2 == 0:
        return 'par'
    else:
        return 'ímpar'

inteiro = int(input('Digite um número: '))

print(f'O número é {verificaNumero(inteiro)}.')

