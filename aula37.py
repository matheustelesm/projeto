frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma.' \
    'Python foi criado por Guido van Rossum.'

i = 0
apareceu = 0
mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if apareceu < qtd_atual:
        apareceu  = qtd_atual
        mais_vezes = letra_atual

   
    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f"{mais_vezes} que apareceu"
    f'{apareceu} x'
)
    
