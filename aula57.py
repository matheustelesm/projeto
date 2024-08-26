# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda'],  # 2
]

# a, b, *_, c = lista
# print(a, c)

# for item in lista:
#     print(item, end=' ')

print(*lista, sep=', ')
print(*string)
print(*tupla)
print(*salas, sep='\n')