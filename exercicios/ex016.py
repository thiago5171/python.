#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da 
#passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input("digite a kilometragem da viagem: "))


if km>200 :
    passagem = km * 0.45
    print("o valor  da passagem foi de {}".format(passagem))
else:
    passagem = km * 0.50
    print("o valor  da passagem foi de {}".format(passagem))
 
print("obrigado pela preferencia")

