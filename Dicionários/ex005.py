'''Contar o número de itens em um dicionário.'''

info = {
    'nome':'Crisitnao',
    'idade':'31',
    'endereco':'Avenida JosÃ© MendonÃ§a de Campos, 800 - ColubandÃª',
    'telefone':'(21) 99999-9999',
    'cidade':'São Gonçalo'
}

soma = 0

for n in info:
    soma += 1
    
print(f'O total de itens no dicionário é {soma}.')
    