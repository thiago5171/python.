"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e 
quantas mulheres têm menos de 20 anos.
"""
vinte= 0
maior = 0
maiorn = ""
somaidade = 0
for i in range(1,5):
    nome = str(input("digite o nome da {}°pessoa: ".format(i)))
    idade = int(input("digite a idade  da {}° pessoa: ".format(i)))
    sexo = str(input("digite o sexo masculino(m) ou feminino(f) [f/m] : "))
    print("")
    somaidade = somaidade + idade
    if sexo == "m":
        if idade > maior :
            maiorn= nome
    else:
         if sexo == "f" :
           if idade <20 :   
               vinte= vinte +1

media = somaidade /4

print("a idade media do grupo é de {} anos ".format(media))
print("o homem mais velho é o {} ".format(maiorn))
print("{} mulheres do grupo tem menos de 20 anos ".format(vinte))

             

