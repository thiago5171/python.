"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""
print("Informe os valores  para saber seu status de acordo com a tabela do imc")
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso/altura**2
print("")
print("De acordo com  a tabela voce esta com ")
if (imc<18.5) :
    print("Abaixo do Peso")
elif (imc > 18.4 and imc < 26 ):
    print("Peso Ideal")
elif (imc > 24 and imc < 30 ):
    print("Sobrepeso")
elif(imc > 30 and imc < 40 ):
    print("Obesidade")
else:
    print("Obesidade Mórbida")
