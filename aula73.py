# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda 1',
    'sobrenome': 'Miranda 2',
    'sobrenome': 'Miranda 3',
    'idade': 18,
}

# pessoa.setdefault('idade', 15) 

# print(pessoa['idade'])

# print(len(pessoa)) 

# print(list(pessoa.keys())) 

# print(tuple(pessoa.values())) 

# print(tuple(pessoa.items())) 

# print(pessoa.get('idade'))

# print(pessoa.pop('nome'))

# print(pessoa.popitem())

# print(tuple(pessoa))

# jeito 1
# pessoa.update({
#     'nome': 'outro valor',
#     'sexo': 'Masculino'
# })

# jeito 2
# pessoa.update(nome='novo valor', sexo='Masculino')
print(pessoa)

# for i in pessoa.items():
#     print(i)