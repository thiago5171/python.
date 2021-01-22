"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
 conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""
n = int(input("digite um numero para ser cnvertido "))
escolha = int(input(" digite 1 para transfornar em binario, 2 para octal, 3 para hexadecimal "))

if (escolha ==1):
    print("o numero convertido para binario é {} ".format(bin(n)))
elif (escolha == 2):
    print("o numero convertido para octal {} ".format(oct(n)))
else:
    print("o numero convertido para hexadecimal {} ".format(hex(n)))