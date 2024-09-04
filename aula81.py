# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for i, valor in pessoa.items():
#     print(i, valor)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6
}

pessoa_completa = {**pessoa, **dados_pessoa}


# print(pessoa_completa)


# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)
    for item, valor in kwargs.items():
        print(item, valor)


# mostro_argumentos_nomeados(nome='Joana', qlq=123)
config = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
    'arg5': 5,
}


mostro_argumentos_nomeados(**config)