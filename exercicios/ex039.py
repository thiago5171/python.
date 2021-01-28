#faça um programa que leia o peso de cinco pessoas. No final, 
#mostre qual foi o maior e o menor peso lidos.
cont = 0
maior = 0
menor = 0
for i in range(1,6):
    peso = float(input())
    if i==1 :
        maior = peso
        menor = peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor = peso



   

print(maior)
print(menor)
    