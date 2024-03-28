# Maior e menor da sequência
#
maior_peso = 0
menor_peso = 0 
#
for pessoa in range(1,6):
    peso = float(input(f'Peso da {pessoa}° pessoa Kg '))
    
    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f'\nO maior peso lido foi de {maior_peso}Kg.')
print(f'O menor peso lido foi de {menor_peso}Kg.')
