"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário 
vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato
"""

gasto = cont = contmil = menor = 0
while True :

    nome = str(input("digite o nome  do produto: "))
    preco = int(input("Digite o preco do produto "))

    gasto += preco
    if cont== 0:
        menor = preco 

    if menor > preco :         
       barato = nome


    if preco >= 1000 :
        contmil += 1

    cont +=1
    continuar = str(input("deseja adicionar outro produto? [S/N] ")).upper()
    if continuar =="N":
        break
print("\n")
print("o total gasto na compra foi {} reais \n"
"{} produto custa mais de 1000 reais \n"
"o nome do produto mais barato é {}".format(gasto,contmil,barato))