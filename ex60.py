# Cálculo do fatorial
#
from math import factorial
#
n = int(input('Digite um número para calcular seu Fatorial: '))
fct = factorial(n)
print(f'O Fatorial de {n} ée {fct}')
#
n1 = int(input('Digite um número para calcular seu Fatorial: '))
c = n1
f = 1
#
print(f'Calculando {n1}! = ',end='')
while c > 0:
    print(f'{c}')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

