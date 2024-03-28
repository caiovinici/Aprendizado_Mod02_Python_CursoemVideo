# Sequência de Fibonacci v1.0
print('Sequência de Fibonacci')
print('xx'*30)
#
n = int(input('Quantos temos você que mostrar? '))
t1 = 0
t2 = 1
# rint('xx'*30)p
#
print(f'{t1} - {t2}', end=' ')
cont = 3
#
while cont <= n:
    t3 = t1 + t2
    print(f' - {t3}', end=' ')
    t1 = t2 # t1 passa a ser a var t2 
    t2 = t3 # t2 passa a ser a var t3
    cont += 1 
print('FIM')
