# Calculando IMC 

peso = float(input('Qual seu peso (KG) '))
altura = float(input('Qual sua altura (M) '))
imc = peso / (altura ** 2)

print(f'\n O seu IMC é de {imc:.1f}')

if imc < 18.5:
    print('Você está \33[4;33m ABAIXO DO PESO normal\033[m')
elif 18.5 <= imc < 25:
     print(f'Você está com \033[4;32m PESO IDEAL, parabéns!\033[m')  
elif 25 <= imc < 30:
     print(f'Você está em \033[4;33 SOBREPESO, fique atento!\033[m')
elif 30 <= imc < 40:
    print('Você está em \033[4;31m OBESIDADE, cuidado!\033[m')
elif imc >= 40:
     print(' Você está em \033[4;31m OBESIDADE MÓRBIDA, ATENÇÃO!\033[m')    
