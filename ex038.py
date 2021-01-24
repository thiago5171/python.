#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas 
#ainda não atingiram a maioridade e quantas já são maiores.
print("digite 7 datas de nascimento, para saber quantas sao menor de  idade, e qunatas sao de maior: ")
cont =0
cont2 = 0
for i in range(0,7,1):
    ano = int(input())
    maior = 2021 - ano
    if (maior <= 18):
        cont = cont + 1
    else:
        cont2 = cont2 + 1

print("{} pessoas sao menor e sao {} maior de idade das 7".format(cont,cont2))