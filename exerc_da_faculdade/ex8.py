#Desenvolva em cada LP um programa leia dois ńúmeros e que pergunte qual operação você deseja realizar. Você 
# deve poder calcular soma (+),subtração (-), multiplicação (*) e divisão  (/).
# Exiba o resultado da operação solicitada.

n1 = float(input("digite o primeiro numero: "))
n2 = float(input(" digite o segundo numero: "))
operacao = int(input("DIGITE UM NUMERO PARA ESCOLHER UMA DAS SEGUINTES OPERAÇÕES"
 "[1] soma (+)"
 "[2] subtração (-)"
 "[3] multiplicação (*)"
 "[4] divisão  (/)"))

    
if operacao== 1:
     soma = n1+n2
     print(f"{n1} + {n2} = {soma}")
elif (operacao == 2):
    subtracao = n1 - n2
    print(f"{n1} - {n2} = {subtracao}")
elif( operacao == 3):
    multip = n1 * n2
    print(f"{n1} x {n2} = {multip}")
elif operacao == 4:
    divisao = n1/n2
    print(f"{n1} / {n2} = {divisao}")  
else:
    print("erro")


  