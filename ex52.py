# Números primos
#
num = int(input('Digite um número: '))

total = 0

for c in range(1,num + 1):
    if num % c == 0: # SINAL DE DIVISÃO % 
        print('\033[30m', end=' ')
        total += 1 
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\033[m -  O número {num} foi divisível {total} vezes')
if total == 2:
    print(f'E por isso ele é PRIMO!')
else:
    print(f'É por isso que ele NÃO é PRIMO!')
