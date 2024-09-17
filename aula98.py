# from sys import path

# import aula98_package
# from aula98_package.modulo import soma_do_modulo
# from aula98_package import modulo
# # print(*path, sep='\n')

# print(soma_do_modulo(5, 6))
# print(aula98_package.modulo.soma_do_modulo(2, 5))
# print(modulo.soma_do_modulo(5, 5))

# from aula98_package.modulo import soma_do_modulo, fala_oi

# print(__name__)

from aula98_package import soma_do_modulo, fala_oi

print(soma_do_modulo(2, 3))
fala_oi()