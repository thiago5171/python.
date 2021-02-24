#Desenvolva  um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário 
# e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = float(input ("digite o valor do salário: "))
aumento = float (input ("digite a porcentagem do aumenta do salário: \n"))
#abaixo eu calculo o valor do aumento, somando o 100 que esta multiplicnado com o valor da porcentagem inputado para calcular o valor total
porcent= (salario*(100+aumento))/100

print(f"o salário que era de R${salario} após o aumento de R${porcent-salario} o salário ficou de R${porcent}")