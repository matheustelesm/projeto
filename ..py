# import pyautogui as bot

# bot.PAUSE = 1.5

# bot.press('win')
# bot.write('google')
# bot.press('enter')

# bot.write('https://chatgpt.com/')
# bot.press('enter')

# bot.write('Como criar um codigo em html')
# bot.press('enter')


#tabuada do número escolhido

# escolha = int(input("Digite um número: "))
# print(f"A tabuada do número {escolha} é:")

# for i in range(1, 11):
#     print(f"{escolha} x {i}: {escolha*i}")


#tabuada 1 ao 10.

# for num in range(1, 11):
#         print(f"\nTabuada do {num}:")
#         for i in range(1, 11):
#             print(f"{num} x {i} = {num * i}")




# 1. Verificar se um número é par ou ímpar
# Escreva um programa que peça ao usuário para inserir um número e determine se esse número é par ou ímpar.

# num = int(input("Digite um número: "))

# if num % 2==0:
#     print("Número par")
# else:
#     print("Número ímpar")




# 2. Fatorial de um número
# Crie um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.

num = int(input("Digite um número: "))

fatorial = 1
for i in range(1, num + 1):
    fatorial *= i
print(f"O fatorial de {num} é {fatorial}")


# 3. Contagem de vogais em uma string
# Crie um programa que peça ao usuário para inserir uma string e conte quantas vogais (a, e, i, o, u) ela contém.

palavra = str(input("Digite uma palavra: "))





# 4. Ordenar uma lista de números
# Escreva um programa que peça ao usuário uma lista de números e a ordene em ordem crescente.

# 5. Palíndromo
# Crie um programa que peça ao usuário uma palavra e verifique se ela é um palíndromo (lida da mesma forma de trás para frente).

# 6. Calculadora Simples
# Escreva um programa que funcione como uma calculadora básica, capaz de somar, subtrair, multiplicar e dividir dois números.