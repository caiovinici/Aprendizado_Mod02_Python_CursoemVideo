# Detector de Palíndromo
#
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # Coloca a frase em Lista exemp -> (['Meu', 'Nome', 'É', 'Caio'])
junto = ''.join(palavras) # Retorna uma string 
inverso = junto[::-1] # Pegando posição 
#
print(f'\nO inverso de {junto} é {inverso}')
#
if inverso == junto:
    print('Temos um Palíndromo!!!')
else:

    print('A frase digitada não é um Palíndromo!')
