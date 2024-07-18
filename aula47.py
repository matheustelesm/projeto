lista = [10, 20, 30, 40]

# del lista[-1]
lista.insert(8000, 5)
print(lista[4])


print("-"*40)

#extender uma lista

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)