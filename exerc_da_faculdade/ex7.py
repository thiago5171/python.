#Desenvolva um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.
preco= float(input("digite o preco  da mercadoria: "))
percent= float(input("digite o percentual de desconto: "))

desconto = (preco * percent)/100
pagar = preco- desconto
print(f"\no valor do desconto foi de R${desconto:.2f}, \ne o preço a pagar foi de R${pagar:.2f}")