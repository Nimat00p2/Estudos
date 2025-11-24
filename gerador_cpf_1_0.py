

import os
import random

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

# Gerando Cpf Aleatorio
    numero_gerado = ''
    for i in range(9):
        numero_gerado += str(random.randint(0, 9))
    
# Calculo do Primeiro
    valor_1 = 0
    multi = 10
    for numero in numero_gerado[:9]:
        valor_1 += int(numero) * multi
        multi -= 1
    valor_final_1 = (valor_1 * 10) % 11
    valor_primeiro = valor_final_1 if valor_final_1 <= 9 else 0
    numero_gerado = numero_gerado + str(valor_primeiro)

# Calculo do Segundo
    valor_2 = 0
    multi = 11
    for numero in numero_gerado[:10]:
        valor_2 += int(numero) * multi
        multi -= 1
    valor_final_2 = (valor_2 * 10) % 11
    valor_segundo = valor_final_2 if valor_final_2 <= 9 else 0
    numero_gerado = numero_gerado + str(valor_segundo)

# Formatação do CPF
    cpf_formatado = numero_gerado[:3] + '.' + numero_gerado[3:6] + '.' + numero_gerado[6:9] + '-' + numero_gerado[9:]

    limpar_tela()
    input(f'Cpf {cpf_formatado} gerado')
