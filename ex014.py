#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre 
#uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite
velocidad = float(input("digite a velocidade que o carro esta: "))

if velocidad >80 :
    velocidad = velocidad-80
    multa = velocidad *7
    print(" voce  ecxedeu o limite de velocidade em {}km/h, o valor  da multa é de R${} .".format(velocidad,multa))
else:
    print("voce esta dentro do limite de velovidade.")
