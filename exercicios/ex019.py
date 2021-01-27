"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
o aumento é de 15%."""

salario = float(input("digite o valor do salario: R$"))
if salario >1250 :
    aumento = (salario * 110)/100
else:
    aumento = (salario*115)/100
print("o salario  inicialmente era de R${} e com o aumneto passou para R${} ".format(salario,aumento))
