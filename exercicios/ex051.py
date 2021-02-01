"""Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual 
será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão 
entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
"""
print("=="*15)
print("          BANCO CEV       ")
print("=="*15)

saque = int(input("Quanto deseja sacar? R$"))
cont50 = cont20 =cont10 = cont = saque1  = saque2= saque3 = 0

while True  :
    if (saque< 50) and (saque > -1):
        if cont50 == 0:
            break
        else:
            print(f" total de {cont50}  cedulas de R$50")
            break
    else:
        saque = saque-50
        cont50 += 1
    

saque1 = saque

while True:
    if (saque1 <20) and (saque > -1):
        if cont20 == 0:
            break
        else:
            print(f" total de {cont20}  cedulas de R$20")
            break
       
    else:
        saque1 = saque1 - 20   
        cont20 +=1 

saque2 = saque1

while True :
    if (saque2 < 10) and (saque2 > -1):
        if cont10 == 0:
            break
        else:
            print(f" total de {cont10}  cedulas de R$10")
            break
    else:
        saque2 = saque2 - 10
        cont10 += 1        

saque3 = saque2
while True :
    if (saque3 == 0):
        if cont == 0:
            break
        else:
            print(f" total de {cont}  cedulas de R$1")
            break
    else:
        saque3 = saque3 - 1
        cont += 1 



print(" Volte sempre ao BANCO CEV! Tenha um bom dia!")




