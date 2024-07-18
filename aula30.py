# exercicios

# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_text = 'ímpar'
    
#     if par_impar:
#         par_impar_text = 'par'

#     print(f'O número {entrada_int} é {par_impar_text}')
    
# else:
#     print('Você não digitou um número inteiro')






# entrada = input('Que horas são?: ')

# try: 
#     hora = int(entrada)

#     if hora >=0 and hora <=11:
#         print('Bom Dia!')
#     elif hora >=12 and hora <=17:
#         print('Boa tarde!')
#     elif hora >=18 and hora <=23:
#          print('Boa noite!')
#     else: 
#         print('Não conheço essa hora :( ')

    


# except:
#       print('Por favor, digite apenas números inteiros')





entrada = input('Digite seu primeiro nome: ')
 
tamanho_nome = len(entrada)

if tamanho_nome > 1:
    if tamanho_nome <=4:
        print('Seu nome é curto')
    elif tamanho_nome >=5 and tamanho_nome <=6:
        print('Seu nome é normal')
    elif tamanho_nome >6:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')
    




    