#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:


from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Ano em que nasceu: '))
idade = ano_atual - ano_nasc

print(f'O atleta tem {idade} anos. ')
 
 #– Até 9 anos: MIRIM
if idade <= 9:
    print(f'A classificação do atleta é MIRIM')
    #– Até 14 anos: INFANTIL
elif idade <= 14:
    print('A classificação do atleta é INFANTIL')    
    #– Até 19 anos: JÚNIOR
elif idade <= 19:
    print('A classificação do atleta é JÚNIOR')
    #– Até 25 anos: SÊNIOR
elif idade <= 25:
    print('A classificação do atleta é SÊNIOR')
    #– Acima de 25 anos: MASTER
else:
    print('A classificação do atleta é MASTER')        

