# Desenvolva em cada LP um programa que leia três números e que imprima o maior e o menor.
a = int(input("digite um numero: "))
b = int(input("digite um numero: "))
c = int(input("digite um numero: "))

maior = menor = a

if menor > b:
    menor = b
if menor > c:
    menor = c
print(f"o menor numero digitado foi {menor}")

if maior < b:
    maior = b
if maior < c:
    maior = c

print(f"o maior numero digitado foi {maior}")