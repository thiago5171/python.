# importaçao da biblioteca para sortear um valor
from random import randint 
pc = randint(0, 5)
numero= int(input("tente adivinhar o valor sorteado de 0 ate 5: "))

if pc== numero:
    print("VOCE ACERTOU!")
else:
    print("VOCE ERROU! ")