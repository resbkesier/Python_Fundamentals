#!/usr/bin/python3

vlr_hora = float(input('Digite o valor da hora: '))
qtd_hora = float(input('Digite a quantidade de horas trabalhadas: '))

salario_bruto = (qtd_hora * vlr_hora)

if salario_bruto >= 4600:
    IR = 27
elif salario_bruto > 3700 and salario_bruto < 4600:
    IR = 22
elif salario_bruto > 2800 and salario_bruto <= 3700:
    IR = 15
elif salario_bruto > 1900 and salario_bruto <= 2800:
    IR = 7
else:
    IR = 0

valorIR = salario_bruto*(IR / 100.0)
valorSindicato = salario_bruto*(3/100.0)
valorFGTS = salario_bruto*(11/100.0)

totalDescontos = valorIR + valorSindicato

salario_liquido = salario_bruto - totalDescontos

print(f'Valor da hora: {vlr_hora}')
print(f'Quantidade de horas trabalhadas: {qtd_hora}')
print(f'Salario Bruto: ({vlr_hora} * {qtd_hora}) R$ {salario_bruto}')
print(f'(-) IR ({IR}%): R${valorIR}')
print(f'(-) Sindicato (3%): R$ {valorSindicato}')
print(f'FGTS (11%): R$ {valorFGTS}')
print(f'Total de Descontos: R$ {totalDescontos}')
print(f'Salario Liquido: R$ {salario_liquido}')

