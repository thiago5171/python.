#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = float(input("digite o valor em metros para saber a conversao em centimetros: "))
conversao = metros*100
print(" {}M  eh igual a {}cm".format(metros,conversao))