"""Desenvolva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de 
cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a 
cada cigarro e calcule quantos dias de vida um fumante perderá. Exiba o total em dias"""
quantidade_pdia= int(input("digite a qunatidade de cigarros fumado por dia: "))
anos =int(input("digite a quantosa anos ja fuma: "))
d_anos= anos*365
tempo= quantidade_pdia*10
dias =((tempo*d_anos)/60)//24
print(f"esse individuo perdeu {dias} dias")