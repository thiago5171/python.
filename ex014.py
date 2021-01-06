# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("digite o valor  de seu salario: "))
aumento = (salario*115)/100
print("o seu salario de R${} com aumento de 15% ficou R${:.2f}".format(salario,aumento))