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

for num in range(1, 11):
        print(f"\nTabuada do {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

