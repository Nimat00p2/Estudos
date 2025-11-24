
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

# Pegando as Informação
    while True:
        try:
            cpf = input('Informe seu cpf: ').replace('.', '').replace('-', '').replace(' ', '')
            quantidade = len(cpf)
            cpf_int = int(cpf)
            if cpf == cpf[0] * 11:
                limpar_tela()
                print('Digitou o mesmo numero')
                continue
            elif quantidade <= 10:
                limpar_tela()
                print('Digitos a menos')
                continue
            elif quantidade == 11:
                break
            else:
                limpar_tela()
                print('Digitos a mais')
                continue
        except ValueError:
            limpar_tela()
            print('Porfavor digite apenas numeros')
        except Exception:
            limpar_tela()
            print('Erro desconhecido')

# Calculo do Primeiro
    valor_validacao_1 = 0
    multi = 10
    for numero in cpf[:9]:
        valor_validacao_1 += int(numero) * multi
        multi -= 1
    valor_final_1 = (valor_validacao_1 * 10) % 11
    validacao_primeiro = valor_final_1 if valor_final_1 <= 9 else 0

# Verificando o Primeiro
    valido_1 = int(cpf[9]) == validacao_primeiro

# Calculo do Segundo
    valor_validacao_2 = 0
    multi = 11
    for numero in cpf[:10]:
        valor_validacao_2 += int(numero) * multi
        multi -= 1
    valor_final_2 = (valor_validacao_2 * 10) % 11
    validacao_segundo = valor_final_2 if valor_final_2 <= 9 else 0

# Verificando o Segundo
    valido_2 = int(cpf[10]) == validacao_segundo

# Formatação do CPF
    cpf_formatado = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]

# Validação
    limpar_tela()
    if valido_1 == True and valido_2 == True:
        print(f'O Cpf {cpf_formatado} é valido')
    else:
        print(f'O Cpf {cpf_formatado} é invalido')
