#Desenvolva em cada LP um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário 
# e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = float(input ("digite o valor do salário: "))
aumento = float (input ("digite a porcentagem do aumenta do salário: \n"))

porcent= (salario*(100+aumento))/100

print(f"o salário que era de R${salario} após o aumento de {aumento}% o salário ficou de R${porcent}")