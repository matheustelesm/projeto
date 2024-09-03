# Exemplo de uso dos sets

letras = set()
while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())

    if 'l' in letra:
        print('Parabéns')
        break
    print(letras)
