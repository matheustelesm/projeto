#nome = 'matheus'
#print(nome[2])
#print(nome[-2])

#print('theus' in nome)
#print ('thus' in nome)

nome = input ('digite seu nome ')
encontrar = input ('digite oque deseja encontrar ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não esté em {nome}')