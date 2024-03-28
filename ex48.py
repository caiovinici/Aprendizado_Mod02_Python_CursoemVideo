# Soma ímpares múltiplos de três 
#
soma = 0 
cont = 0 
#
# Calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
for c in range(1,501,2): 
    if c % 3 ==0: # pegando números multiplos de 3 
        soma += c
        cont += 1
print(f'A soma de todos os {cont} valores solictados {soma}')

