# Decoradores com parâmetros

# def fabrica_de_decoradores(a=None, b=None, c=None):
#     def fabrica_de_funcoes(func):
#         print('Decoradora 1')

#         def aninhada(*args, **kwargs):
#             print('Aninhada')
#             res = func(*args, **kwargs)
#             return res
#         return aninhada
    
#     return fabrica_de_funcoes
# @fabrica_de_decoradores(1, 2, 3)
# def soma(x, y):
#     return x + y

def validar(funct):
    def valida(x, y):
        if x <0 or y <0:
            raise ValueError("x e y não podem ser negativos.")
        x*= 2
        y*=2
        return funct(x, y)
    
    return valida


@validar
def soma(x, y):
    return x+y


somar = soma()
print(somar)





