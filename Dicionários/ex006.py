'''Verificar se um determinado atributo está presente em um dicionário.'''

info = {
    'nome':'Crisitnao',
    'idade':'31',
    'endereco':'Avenida JosÃ© MendonÃ§a de Campos, 800 - ColubandÃª',
    'telefone':'(21) 99999-9999',
    'cidade':'São Gonçalo'
}

for i in info.keys():
    if i == 'cidade':
        print(f'A chave {i} foi encontrada no dicionário.')
    