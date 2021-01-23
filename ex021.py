"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor
da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode 
exceder 30% do salário ou então o empréstimo será negado.
"""
salario = float(input("digite o valor do seu salario: "))
anos = int(input("em qunatos anos voce quer pagar: "))
emprestimo = float(input("digite o valor  da casa: "))
porcentagem = (salario * 30)/100

prestacao = (emprestimo/anos)/12
if (prestacao > porcentagem) :
     mensagem = "REPROVADO"
else:
    mensagem = "APROVADO"

print(" o emprestimo de {} em {} anos com  a prestacao mensal de {:.2f} foi {} ".format(emprestimo,anos,prestacao,mensagem))