# Soma dos pares
#
# Pegando os 6 valores para somar
somar = 0
cont = 0
#
for c in range(1,7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0: # % 2 ==0 - números PARES
        somar += num
        cont += 1
print(f'Você informou {cont} números PARES e a soma foi {somar}.')

