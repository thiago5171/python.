"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""
termo = int(input(" digite o primeiro termo de uma PA: "))
razao = int(input("digite a razao dessa PA: "))

for i in range(1,10):
    print(termo)
    termo = termo + razao