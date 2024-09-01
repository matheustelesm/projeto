pessoa = {}

chave = 'nome'
pessoa[chave] = 'Matheus Teles'
pessoa['sobrenome'] = 'Santanna'



print(pessoa[chave])
pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

