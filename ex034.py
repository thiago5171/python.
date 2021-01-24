#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
#Se o valor digitado for ímpar, desconsidere-o.

print("digite seis numero")
soma = 0 
for i in range(0,6):
    numero = int(input())
    if (numero%2==0):
        soma = soma +numero

print("a soma dos numeros pares são: ",soma)

