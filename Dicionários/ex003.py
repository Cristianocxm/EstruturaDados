''' Remover um item de um dicionário existente.'''

info = {
    'nome':'Crisitnao',
    'idade':'31',
    'endereco':'Avenida José Mendonça de Campos, 800 - Colubandê',
    'telefone':'(21) 99999-9999',
    'cidade':'São Gonçalo'
}

info.pop('cidade')

print(info)