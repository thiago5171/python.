#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.


valido = False
#poderia ter usado while not in "mMfF": que funcionaria da mesma forma
while valido  == False :
# esse[0] é para o programa pegar so a primeira string, strip é para tirar os espaços e upper para coloca tudo em maiusculo
    sexo = str(input("informe se sexo [M/F]:  ")).strip().upper()[0]
    if sexo == "F" or (sexo == "M"):
        valido = True
    else:
        valido = False
        print("dados invalidos, por favor informe seu sexo")
        
if sexo == "M":
    print("sexo Masculino registrado com sucesso ")
else:
    print("sexo Feminino registrado com sucesso ")
