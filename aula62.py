"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y): #<-- parâmetros 
    print(f"{x = } {y = } | x + y = {x+y}")

soma(5, 6) #<-- argumentos posicionais
soma(y=6, x=5)#<-- argumentos nomeados
soma(x=5, y=6)