#calculadora com while
while True: 
    numero_1 = input('Digite um número: ')
    operador = input('Digite um operador básico: ')
    numero_2 = input('Digite outro número: ')
   
    numer_validos = None
    numero_1_float = 0
    numero_2_float = 0
    try:
        numero_1_float = int(numero_1)
        numero_2_float = int(numero_2)
        numer_validos = True
    except:
         numer_validos = None
        

    if numer_validos is None:
        print('Um ou ambos dos números não são válidos, tente novamente')
        continue

    opera_permitidos = '+-*/'

    if operador not in opera_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando sua conta, confira o resultado abaixo')

    if operador == '+':
        print(f'{numero_1_float}+{numero_2_float}=', numero_1_float + numero_2_float)
    elif operador == '-':
         print(f'{numero_1_float}-{numero_2_float}=', numero_1_float - numero_2_float)
    elif operador == '/':
        print(f'{numero_1_float}/{numero_2_float}=', numero_1_float / numero_2_float)
    elif operador == '*':
        print(f'{numero_1_float}*{numero_2_float}=', numero_1_float * numero_2_float)
    else:
        print('Tudo vólts')

    #########
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
   
    if sair is True:
        print('vsf,tmj')
        break
  
    