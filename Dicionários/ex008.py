'''Percorrer todos os itens em um dicionário e imprimir os atributos e valores.'''

info = {
    'Nome':'Crisitnao',
    'Idade':'31 anos',
    'Endereco':'Avenida JosÃ© MendonÃ§a de Campos, 800 - ColubandÃª',
    'Telefone':'(21) 99999-9999',
    'Cidade':'São Gonçalo'
}

for k,v in info.items():
    print(f'{k} : {v}')

