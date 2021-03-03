"""Desenvolva em cada LP um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para 
comércios. Calcule o preço a pagar de acordo com a tabela a seguir:
"""
kwh = float(input("digite a quantidade de kWh consumida: "))
instalacao =str(input("digite o tipo de instalação: \nR para residências \nI para indústrias  \nC para comércios\n")).upper()

if instalacao =="R":
    if kwh >500:
        pagar=  kwh*0.65
    else:
        pagar= kwh *0.40
elif instalacao =="C":
    if kwh >1000:
        pagar=  kwh*0.60
    else:
        pagar= kwh *0.55
elif instalacao =="I":
    if kwh >5000:
        pagar=  kwh*0.55
    else:
        pagar= kwh *0.60
else:
    print("erro")
print(f"o preco total a pagar foi de R${pagar:.2f}")
        