# Maior e Menor valores
opc = 'S'
soma = quant = med = maior = menor = 0 # variaveis que recebem o mesmo valor 
#
while opc in 'S':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1 
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opc = str(input('Quer continuar? [S/N]: ')).upper().strip() [0]
#
med = soma / quant
print(f' Você digitou {quant} e a média foi {med:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
nome = str
idade = int


