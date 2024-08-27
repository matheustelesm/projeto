# cpf_enviado_pelo_usuario = '746.824.890-70'.replace('.', '').replace('-', '').replace(' ', '')
# #replace: substitui um coisa por outra.
import re # = substitui 
import sys

entrada = input('Por favor, digite seu CPF: ')
cpf_enviado_pelo_usuario = re.sub(r'[^0-9]', '', entrada)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_pelo_usuario[:9]
contador_regressivo1 = 10

resultado_digito1 = 0
for digito in nove_digitos:
    resultado_digito1 += int(digito) * contador_regressivo1
    contador_regressivo1 -= 1
digito_1  = (resultado_digito1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


dez_digitos = cpf_enviado_pelo_usuario[:10]
contador_regressivo2 = 11

resultado_digito2 = 0
for digito in dez_digitos:
    resultado_digito2 += int(digito) * contador_regressivo2
    contador_regressivo2 -=1
digito_2 = (resultado_digito2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_calculado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_calculado == cpf_enviado_pelo_usuario:
    print(f'O CPF {cpf_enviado_pelo_usuario} é válido')
else:
    print(f'O CPF é inválido')  