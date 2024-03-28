# Criando um Menu de Opções
import os
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opc = 0
print('xx'*25)
#
while opc !=5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opc = int(input('Qual sua opção: '))
#
    if opc == 1:
        soma = n1 + n2
        print(f'A somar entre {n1} e {n2} é = {soma}')
    elif opc == 2:
        produto = n1 * n2
        print(f'A somar entre {n1} e {n2} é = {soma}')
    elif opc == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2    
        print(f'O número MAIOR entre {n1} e {n2} é o {maior}')
    elif opc == 4:
        os.system('cls')
        print('Informe os números novamente!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opc == 5:
        print('Finalizando...!')
    else:
        print('Opção inválida, Tente novamente.')
print('xx'*25)
#
print('Fim do programa! Volte sempre.')




