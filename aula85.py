lista = []
for i in range(3):
    for y in range(3):
        lista.append((i, y))


lista = [(i, y) for i in range(3) for y in range(3)]
    
print(lista)