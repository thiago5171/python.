"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando 
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram 
digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
soma = 0
parada=False
cont = 0
while parada == False: 
    num = int(input("digite um numero [999 para parar]: "))
    if num !=999 :
        cont +=1 
        soma += num
    else:
        parada = True
print("voce digitou {} numeros e a soma entre ele é {}.".format(cont,soma))