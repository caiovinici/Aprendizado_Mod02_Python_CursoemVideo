# Progressão Aritmética v2.0

print('Gerador de PA')
print('xx'*10)
#
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
#
while cont <= 10:
    print(f'{termo} - ', end='')
    termo += razao
    cont += 1 
#
print('FIM')
