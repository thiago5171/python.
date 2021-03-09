"""Desenvolva em cada LP um programa que calcule o resto da divisão inteira entre dois números. Utilize 
apenas as operações de soma e subtração para calcular o resultado.
"""
dividendo=int(input("digite o numero do dividendo: "))
divisor=int(input("digite o numero do divisor: "))
cont=0

for i in range(1,dividendo+1,divisor):
    cont+=1

if dividendo%2==1:
    print(f"o resultado da divisão foi {cont-1}")
else:
    print(f"o resultado da divisão foi {cont}  ")
