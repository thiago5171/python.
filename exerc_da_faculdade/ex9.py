"""Desenvolva em cada LP um programa para aprovar o empréstimo bancário para compra de uma casa. O programa 
deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação 
mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a 
comprar dividido pelo número de meses a pagar.
"""
casa = float(input("digite o valor da casa: "))
salario = float(input("digite o valor do seu salario: "))
anos = int(input("em quantos anos deseja pagar: "))
ano=anos*12
prestacao=casa/ano
porcent = (salario*30)/100
if prestacao> porcent:
    print("EMPRESTIMO NEGADO")
else:
    print("EMPRESTIMO APROVADO")