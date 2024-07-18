import os

palavra_secreta = 'secreta'
acertos = ''
tentativas = 0
while True:

    letra = input('Digite uma letra: ')
    tentativas += 1

    if len(letra) > 1:
        print('Digite apenas UMA letra!') 
        continue

    if letra in palavra_secreta:
        acertos += letra

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in acertos:
            palavra_formada += letra_secreta
        
        else:
            palavra_formada += '*'

    print('palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Você ganhou!!')
        print('A palavra era', palavra_formada)
        print(f'Você tentou {tentativas} vezes')
        acertos = ''
        tentativas = 0