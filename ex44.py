# Parcelamento 

print('= = = = \033[1;40m COMPRAS = ONLINE\033[m = = = = ')
#
lista_produto = ['[1] HeadSet', '[2] PSP', '[3] Iphone 15 Pro Max']
preco = [599, 430, 12500]
#
# selecionar item da lista 
prodt_select = int(input(f'\n\033[1;40mSELECIONE O PRODUTO\033[m:\n{lista_produto}: '))
prodt_cliente = lista_produto[prodt_select -1]
print('')
#
# informar item e valor do produto selecionado na lista 
preco_select = preco[prodt_select -1]
print(f'\033[1;40m PRODUTO SELECIONADO\033[m: {prodt_cliente} R$ {preco_select:.2f}')
#
# escolhar de pagamentos 
print('\n\033[1;40m SELECIONE A FORMA DE PAGAMENTO\033[m')
print('''\033[33m[1] À VISTA DINHEIRO/PIX 
[2] À VISTA CARTÃO DÉBITO
[3] 2x NO CARTÃO DE CRÉDITO
[4] 3X OU MAIS NO CARTÃO DE CRÉDITO\033[m''')
# 1 10% DESCONTO // 2 5% DESCONTO // 3 VALOR FORMAL  // 4 20% DE JUROS
#
forma_pag = int(input('\033[1;40m OPÇÃO\033[m: '))
#
#
if forma_pag == 1:
    total = preco_select - (preco_select * 10 / 100) # 10%
    print(f'\nSua compra de R$\033[32m {preco_select:.2f} \033[m, com \033[4m 10% de desconto \033[m sairá por R$\033[32m{total:.2f}\033[m')
elif forma_pag == 2:
    total = preco_select - (preco_select * 5 / 100) # 5%
    print(f'Sua compra de R$\033[32m{preco_select:.2f}\033[m, com \033[4m 5% de desconto\033[m sairá por R$\033[32m {total:.2f} \033[m')
elif forma_pag == 3:
    total = preco_select
    parcelas_2 = total / 2 
    print(f'Sua compra de R$\033[332m {preco_select:.2f} \033[m, parcelada em \033[4m 2x SEM JUROS \033[m de R$\033[32m {parcelas_2:.2f}\033[m')
elif forma_pag == 4:
    total = preco_select + (preco_select * 20 / 100)
    total_parcelas = int(input('\033[1;40m Em quantas vezes deseja parcelar?\033[m'))
    parcelas = total / total_parcelas
    print(f'Sua compra de R$\033[32m{preco_select:.2f}\033[m será parcelada em \033[4m {total_parcelas}x \033[m com \033[4m JUROS \033[m de R$\033[32m{parcelas:.2f}\033[m')  
else:
    total = preco_select
    print('\033[1;31m OPÇÃO DE PAGAMENTO INVÁLIDA, TENTE NOVAMENTE!\033[m')
print(f'Sua compra de R${preco_select:.2f} passou á custar R${total:.2f} no final.')
 
