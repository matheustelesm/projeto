# Try, except, else e finally


string = 'Matheus'
print(isinstance(string, str))

try:
    a = 18
    b = 0   
    # print(b[0])
    c = a/b
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print('impossivel dividir por zero.')

except NameError:
    print('Algum nome não está definido, verifique o código')

except (TypeError, IndexError) as error:
    print('Ocorreu um TypeError OU IndexError')
    print('MSG: ', error)
    print('Nome: ', error.__class__.__name__)

except Exception:
    print('Erro desconhecido, verifique o código')



print('Continuar')