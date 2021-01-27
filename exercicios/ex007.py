#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada(usando enquanto)
v = int(input(" digite um valor para ter sua tabuada: "))
n = 1
while n<11:
     print("{} x {} = {} ".format(v,n,v*n))
     n = n+1