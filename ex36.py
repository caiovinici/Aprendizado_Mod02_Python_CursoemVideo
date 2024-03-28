# Aprovação Bancaria

print('*-*'*35)

print('= = = CENTRAL DE EMPRÉSTIMOS BANCÁRIO = = =')

print('*-*'*35)

print('\n \033[1;40m Informe os dados abaixo para simular o empréstimo \033[m')
print('--'*35)

from time import sleep
import getpass


nome_comprador = str(input('\n* \033[33m Nome do comprador(a): \033[m')).strip().title()
#cpf = int(input('* CPF do comprador: '))

salario = float(input('*\033[33m Salário do comprador(a): \033[m R$ '))
valor_casa = float(input('* \033[33m Valor da casa desejada: \033[m R$ '))
anos = int(input('* \033[33m Em quantos anos deseja quitar: \033[m '))

sleep(1)

prestacao = valor_casa / (anos * 12)
minimo = salario * 30 / 100 # 30%

print('--'*35)
print('\033[1;40m AGUARDE UM MOMENTO ESTAMOS ANALISANDO SEUS DADOS PARA FINANCIAMENTO \033[m')
print('--'*35)

sleep(2)

print(f'O comprador(a) {nome_comprador}')
print(f'Conforme o valor da casa de R$ \033[32m {valor_casa:.2f} \033[m com pagamento de \033[3m{anos} anos\033[m, as parcelas será de R$ \033[32m {prestacao:.2f} \033[m.')

if prestacao <= minimo:
    print('Empréstimo  \033[2;32m APROVADO !!! \033[m')
else:
    print('Empréstimo \033[2;31m NÃO AUTORIZADO X \033[m !! ')


# valor da casa
# salario do comprador
# quantas parcelas
# prestação nao pode exceder 30% do salario
    

