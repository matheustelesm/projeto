# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set('ola')  # vazio # é uma class
# s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# s1 = set([1, 2, 3, 3, 4, 4, 5, 5])
# li = list(s1)
# print(li)

# s1 = {1, 2, 3, 4}
# print(4 in s1)  # para buscar algo que está dentro do set, como nao tem index usamos isso.
# for numero in s1:
#     print(numero)

# a = type([1, 2, 3])                   # list --> mutável
# b = type({1, 2, 3})                   # set --> mutável
# c = type((1, 2, 3))                   # tuple --> tuple imutável
# d = type({ '1': 1, '2': 2, '3': 3})   # dict --> mutável


# print(a, b, c, d)

# Métodos úteis:
# add --> adiciona um item no set, update --> adiciona um iteravel no set, clear --> limpa o set, discard --> descarta algum valor do set

# s1 = set()
# s1.add('Matheus')
# s1.add(1)
# s1.add(2)
# s1.update(('Ola, Mundo', 1, 2, 3))
# # s1.clear()
# s1.discard('Ola, Mundo')
# s1.discard('Matheus')
# print(s1)


# Operadores úteis:

# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # --> Une os sets sem repetir itens
s4 = s1 & s2 # --> Itens presentes em ambos
s5 = s2 - s1 # --> Itens presentes apenas no set da ESQUERDA
s6 = s1 ^ s2 # --> Itens que não estão em ambos

print(s3)
print(s4)
print(s5)
print(s6)