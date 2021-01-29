"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média 
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se 
ele quer ou não continuar a digitar valores.
"""
cont=0
soma=0
continuar = "S"
while continuar == "S":
    num = int(input("digite um numero: "))
    continuar = str(input("deseja continuar? [S/N]")).upper()
    soma+=num
    if cont==0:
        maior=num
        menor=num
    else:
        if maior<num:
            maior = num
        if menor > num:
            menor = num

    cont += 1
media = soma / cont

print("a media entre todos os valor  foi de {:.2f} \n"
"o miaor valor foi {} \n"
"o menor valor foi {}".format(media,maior,menor))

