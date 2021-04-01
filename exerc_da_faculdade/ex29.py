# Receba duas frases distintas e imprima de maneira invertida, trocando as letras A por *.
frase1=input("->").upper()
frase2= input("->").upper()
invertida1 = frase1[::-1]
invertida2= frase2[::-1]
invertida1=invertida1.replace("A","*")
invertida2=invertida2.replace("A","*")

print("primeira invertida->",invertida1)
print("segunda invertida->",invertida2)