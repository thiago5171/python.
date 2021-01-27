"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
"""

valor = float(input("Digite o preco do produto: "))

pagamento = int(input("escolha sua forma de pagamento digitendo o numero a sua esquerda, e tera os respectivos descontos\n"
      "[1] à vista dinheiro/cheque: 10% de desconto\n"
      "[2] à vista no cartão: 5% de desconto\n"
      "[3] em até 2x no cartão: preço formal\n"
      "[4] 3x ou mais no cartão: 20% de juros\n "))
print("")
if pagamento == 1 :
    desconto = (valor * 90)/100
elif pagamento == 2:
    desconto = (valor * 95)/100
elif pagamento == 3:
    desconto = valor
else:
    desconto = valor*0,20*3

print(" valor total a ser pago de acordo com o metodo escolhido é {} reais".format(desconto))
