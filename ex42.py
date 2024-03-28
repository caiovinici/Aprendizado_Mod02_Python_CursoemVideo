# Exercício 42 – Analisando Triângulos v2.0
#
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem FORMAR um triângulo', end='')
    if a == b == c:
        print('EQUILÁTERO!') #  EQUILÁTERO: todos os lados iguais
    elif a != b != c != a:
        print('ESCALENO') # ESCALENO: todos os lados diferentes
    else:
        print('ISÓSCELES') # ISÓSCELES: dois lados iguais, um diferente
else:
    print('Os segmentos acima NÃO podem FORMAR um triângulo')

