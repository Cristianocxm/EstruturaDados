'''Agrupar informações relacionadas em um único dicionário, como informações
de contato de várias pessoas.'''


contatos = {}


while True:
    pessoa = input('Digite seu nome, ou aperte x para sair: ')
    if pessoa == 'x':
        break
    else:
        telefone = input('Digite seu telefone no formato (xx) xxxxx-xxxx: ')
        contatos.update({pessoa:telefone})

print(contatos)
    

