'''Obter o valor de um determinado atributo em um dicionário.'''

info = {
    'nome':'Crisitnao',
    'idade':'31',
    'endereco':'Avenida JosÃ© MendonÃ§a de Campos, 800 - ColubandÃª',
    'telefone':'(21) 99999-9999',
    'cidade':'São Gonçalo'
}

for k,v in info.items():
    if k == 'cidade':
        print(f'O valor de {k} é: {v}.')