#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias =int(input("quantos dias  alugados? "))
km= float(input("quantos km rodados? "))
rdias= dias*60
rkm= km*0.15
print("o valor a pagar é de {:.2f}".format(rdias+rkm))