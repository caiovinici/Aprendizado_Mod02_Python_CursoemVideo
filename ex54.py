# Grupo da Maioridade 21+
#
from datetime import date
ano_atual = date.today().year
#
total_maior = 0 # variavel qe guarda o valor de maior idade
total_menor = 0 # variavel qe guarda o valor de menor idade
#
for pess in range(1,8):
    ano_nasc = int(input(f'Em que ano a {pess}° pessoa nasceu? - '))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print(f'\nAo todo tivemos {total_maior} pessoas maiores de idade')
print(f'E também {total_menor} pessoas menores de idade')
        