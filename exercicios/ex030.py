"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
 artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

#importar a bliblioteca para esperar 
from time import sleep

print("contagem regressiva para os fogos!!!!")
for a in range(10,0,-1):
   print(a) 
   sleep(1)
print("FOGOS")