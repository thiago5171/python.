"""Desenvolva em cada LP um programa que calcule o resto da divisão inteira entre dois números. Utilize 
apenas as operações de soma e subtração para calcular o resultado.
"""
dividendo=int(input("digite o numero do dividendo: "))
divisor=int(input("digite o numero do divisor: "))

while dividendo>=divisor:
    dividendo= dividendo-divisor


print(f"o resto eh => {dividendo}")
    
