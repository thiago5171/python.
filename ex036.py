# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

soma = 0

n = int(input("digite um numero para saber se ele eh primo:  "))

for i in range(1, n + 1):
    print("{}".format(i), end=' ')
    if (n % i == 0):
        soma = soma + 1

if (soma == 2):
    print("o numero {} foi divisivel 2 vezes \n e por isso ele é primo".format(n))
else:
    print("o numero {} foi divisivel {} vezes \n e por isso ele  nao é primo".format(n, soma))
