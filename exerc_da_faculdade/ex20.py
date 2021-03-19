#jogo de adivinhação
import os
import time
n=int(input("insira um numer: "))
time.sleep(1)

os.system("cls")#comando para limpar a tela
print("tente adivinhar o numer  digitado anteriormente")
u=-1
while n!=u:
    u=int(input("->"))
    if n<u:
        print("O numero correto eh menor ")
    if n>u:
        print(" o numero correto eh maior")

print("PARABENS!! VOCE ACERTOU")  