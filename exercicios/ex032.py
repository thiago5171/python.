"""Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que
 se encontram no intervalo de 1 até 500.
"""
print("a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500 é:")
soma=0
for i in range(1,501,1) :
    if (i%3==0):
        soma= soma + i

print(soma)