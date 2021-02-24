""" Desenvolva  um programa que solicite o preço de uma mercadoria e o percentual de desconto.
 Exiba o valor do desconto e o preço a pagar."""
 
preço= float (input ("digite o valor da mercadoria: "))
desconto= float (input ("digite a porcentagem do desconto desse produto: "))
#calculo abaixo apenas de quanto sera o valor do descontado
descontado = ( preço* desconto)/100
#calculo do preco a pagar apos o desconto
Pagar= preço- descontado

print(f"\no valor do desconto foi de R${descontado}, e o preço total a pagar do produto foi de  R${Pagar}")
