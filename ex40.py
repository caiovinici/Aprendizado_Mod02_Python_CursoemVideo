# Média de Classe

aluno = str(input('Nome do aluno(a): '))
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

print(f'\n O aluno(a) {aluno}, tirou {n1:.1f} primeira nota e {n2:.1f} segunda nota a média foi de {media:.1f}')

if media >= 7:
    print(f'O aluno(a) {aluno}, está APROVADO ! ')
    
elif media < 5:
    print(f'O aluno(a) {aluno}, está REPROVADO !')

elif media >= 5 and media < 7:
    print(f'O aluno(a) {aluno}, está de RECUPERAÇÃO ! ')



#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO