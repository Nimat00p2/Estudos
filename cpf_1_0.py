
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

    valor_1 = 0
    valor_2 = 0
    valido_1 = False
    valido_2 = False

# Pegando as Informação
    while True:
        try:
            cpf_str = input('Informe seu cpf: ').replace('.', '').replace('-', '').replace(' ', '')
            quantidade = len(cpf_str)
            cpf = int(cpf_str)
            for i in cpf_str:
                maximo = cpf_str.count(i)
            if maximo == quantidade:
                limpar_tela()
                print('Digitou o mesmo numero')
                continue
            elif quantidade <= 10:
                limpar_tela()
                print('Digitos a menos')
                continue
            elif quantidade == 11:
                cpf_completo = (cpf_str[:9]) + '-' + (cpf_str[9:])
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
    CPF = cpf_completo.split('-')

# Calculo o Primeiro
    for i, numero in enumerate(CPF[0], -10):
        valor_1 += int(numero) * abs(i)
    valor_final_1 = (valor_1 * 10) % 11
    validacao_primeiro = valor_final_1 if valor_final_1 <= 9 else 0

# Verificando o Primeiro
    for i, numero in enumerate(CPF[1][0]):
        if int(numero) == validacao_primeiro:
            valido_1 = True

# Calculo o Segundo
    for i, numero in enumerate(CPF[0], -11):
        valor_2 += int(numero) * abs(i)
    valor_final_2 = (((validacao_primeiro * 2) + valor_2) * 10) % 11
    validacao_segundo = valor_final_2 if valor_final_2 <= 9 else 0

# Verificando o Segundo
    for i, numero in enumerate(CPF[1][1]):
        if int(numero) == validacao_segundo:
            valido_2 = True

# Validação
    limpar_tela()
    if valido_1 == True and valido_2 == True:
        print(f'O Cpf {cpf_completo} é valido')
    else:
        print(f'O Cpf {cpf_completo} é invalido')
