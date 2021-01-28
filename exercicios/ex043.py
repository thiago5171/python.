"""Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

num = int(input(" digite um numero para saber seu fatorial: "))
print("num")
cont = num

fatorial = 1

print("{}! = ".format(num,num), end=' ')

while cont != 0:
#é necessario esse if para que  o x de multiplicacao so apareça apos o primeiro valor do fatorial aparecer
# e nao apareça algo do tipo x7x8 = 56
    if cont == num:
        print("{}".format(cont), end=' ')
    else:
        print("x {}".format(cont), end=' ')

    fatorial = fatorial * cont
    cont =  cont -1


print("= {}".format(fatorial))































