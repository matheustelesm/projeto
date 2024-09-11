"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

# print('Valor' if False else 'Outro valor')

# condicao = 10 == 100
# var = 'Valor' if condicao else 'Outro valor'
# print(var)

# digito = 9 # > 9 = 0 
# novo_digito = digito if digito <= 9 else 0 
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)

# print('Valor' if False else 'Outro valor' if False else 'fim')

precos = [100, 200, 400 , 1500, 2000]

def imposto(preco):
    return preco * 0.5

imposto2 = list(map(imposto, precos))
print(imposto2)