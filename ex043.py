"""Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

num = int(input(" digite um numero para saber seu fatorial: "))
print("num")
cont = num
fatorial = 1
print("{}! = ".format(num), end=' ')
while cont != 0:
    print("{} x".format(cont), end=' ')
    fatorial = fatorial* cont
    cont =  cont -1


print("= {}".format(fatorial))































