##Desafio 13: Faça um algoritmo que leia o salário de um funcionário e
# mostre seu novo salários, com 15% de aumento.

salario = float(input('Qual é o salário do Funcionário? R$ '))

novo_salario = float(salario * 1.15)

print(f'Um funcionário que ganhava R$ {salario:.2f}, com 15% de aumento, passa a receber: R$ {novo_salario:.2f}'.format())