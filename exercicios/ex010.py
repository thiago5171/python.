#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("digite o valor do produto: "))
desconto = (preco*95)/100
print("o valor do produto com 5% de desconto é R%{}.".format(desconto))
