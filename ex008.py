#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input("quantos reais voce tem na carteira: R$"))
dolar =  real/5.31
print("com R${:.2f}  voce pode comprar U${:.2f}.".format(real,dolar))