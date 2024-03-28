# Alistamento Militar 

from datetime import date # importa ano e data atual do pc 

ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc # DESCOBRINDO IDADE DA PESSOA PELO ANO 
print('=-' * 1)

print(f'Você nasceu em {ano_nasc} tem {idade} anos em {ano_atual}')

if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
        saldo = 18 - idade
        print(f'Ainda falta {saldo} anos para o ALISTAMENTO MILITAR')
        ano = ano_atual + saldo
        print(f'Seu alistamento será em {ano}')
elif idade > 18:    
        saldo = idade - 18    
        print(f'Você já deveria ter se ALISTADO há {saldo} anos')
        ano = ano_atual - saldo
        print(f'Seu alistamento foi em {ano}')
