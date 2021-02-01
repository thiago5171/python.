"""
Crie um programa que leia a "idade" e o "sexo" de várias pessoas. A cada pessoa cadastrada, o programa deverá 
perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
"""
conth = cont18 = cont20 = 0

while True :

    idade = int(input("Qual sua idade? "))
    sexo = str(input("Qual o seu sexo [M/F]? ")).upper()

    if sexo=="M":
        conth += 1
        if  idade > 18:
            cont18 += 1
    
    if (sexo =="F") and (idade < 20) :
            cont20 = cont20 +1

    continuar = str(input("deseja continuar? [S/N] ")).upper()
    if continuar == "N":
        break

    
print("{} homem tem mais de 18 anos \n"
"{} homem foram cadastrados \n"
"{} mulheres tem menos de 20 anos ".format(cont18,conth,cont20))