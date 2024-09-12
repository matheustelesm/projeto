# Try, except, else e finally
# try não pode ficar sozinho, no minino try e except ou finally
# except, else e finally não vem sozinhos
# sempre começar com o try

try:
    print('Abrir arquivo')
    8/0

except ZeroDivisionError:   # trata a exceção
    print('Dividiu por zero')

else:
    print('Não deu erro')

finally:
    print('Fechar Arquivo')

