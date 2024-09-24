# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]



# def zipper(lista1, lista2):
#     intervalo_maximo = min(len(lista1), len(lista2))
#     return [(lista1[i], lista2[i]) for i in range(intervalo_maximo)]


# lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# lista2 = ['BA', 'SP', 'MG', 'RJ']

# print(zipper(lista1, lista2))
from itertools import zip_longest


# lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# lista2 = ['BA', 'SP', 'MG', 'RJ']
# print(list(zip_longest(lista1, lista2, fillvalue="SEM CIDADE")))
# print(list(zip(lista1, lista2)))

# l1 = [1, 2, 3, 4, 5, 6, 7]
# l2 = [1, 2, 3, 4]
# l = []
# for i in range(len(l2)):
#     l.append(l1[i] + l2[i])

# print(l)


# l1 = [1, 2, 3, 4, 5, 6, 7]
# l2 = [1, 2, 3, 4]
# l = []
# for i, _ in enumerate(l2):
#     l.append(l1[i] + l2[i])

# print(l)
# com o zip_longest
from itertools import zip_longest
l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip_longest(l1 , l2, fillvalue=0)]
print(lista_soma)

#com o zip
l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip(l1 , l2)]
print(lista_soma)