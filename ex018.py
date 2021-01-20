#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

a = int(input("digite um numero: "))
b = int(input("digite um numero: "))
c = int(input("digite um numero: "))
print("")
print("METODO 1")
# para saber quantos se serao necessario é preciso fazer um calculo de analise combinatoria 3!
# que seria 3*2*1 = 6


if (a > b) and (b > c) and (a > c):
 print("o maio é {} e o menor é {}".format(a,c))
else:
    if (a > c) and (c > b) and (a > b):
     print("o maio é {} e o menor é {}".format(a,b))
    else:
        if (b > a) and (a > c) and (b > c) :
             print("o maio é {} e o menor é {}".format(b,c)) 
        else: 
            if (b > c) and (c > a ) and (b > a) :
             print("o maio é {} e o menor é {}".format(b,a)) 
            else: 
                if (c > a) and (a > b) and (c > b) :
                 print("o maio é {} e o menor é {}".format(c,b))
                else: 
                     if (c > b) and (b > a) and (c > a) :
                        print("o maio é {} e o menor é {}".format(c,a))



print("="*50)
#tambem é possivel fazer de outra forma mais curta
print("METODO 2")
menor = a
if (b<a) and (b<c):
   menor = b
if (c<a) and (c<b):
    menor = c
print(" o menor é {}".format(menor))
maior = a
if (b>a) and (b>c) :
    maior = b 
if (c>a) and (c>b) :
    maior = c
print(" o maior é {}".format(maior))