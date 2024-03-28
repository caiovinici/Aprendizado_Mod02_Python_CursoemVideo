# Progressão Aritmética
#
primeiro_termo = int(input('Primeiro Termo:')) # inicio da contagem
razao = int(input('Razão:')) # contando de x razao 
decimo = primeiro_termo + (10 - 1) * razao
#
for c in range(primeiro_termo, decimo + razao, razao):
    print(f'{c}', end='- ')
print('ACABOOU!')
