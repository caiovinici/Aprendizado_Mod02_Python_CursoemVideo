# Conversor de Bases Numéricas 

num = int(input('Digite um número inteiro: '))

print('''Escolhar uma das opções;
      [ 1 ] converter para BINÁRRIO
      [ 2 ] converter para OCTAL
      [ 3 ] converter para HEXADECIMAL''')

opcao = int(input('Sua opção é: '))

if opcao == 1:
    print(f'O {num} convertido para BINÁRIO É  {bin(num)[2:]}.')
elif opcao == 2:
    print(f'O {num} convertido para OCTAL é {oct(num)[2:]}.')
elif opcao == 3:
    print(f'O {num} convertido em HEXADECIMAL é {hex(num)[2:]}.')
else:
    print('Opção inválida, Tente novamente !')

