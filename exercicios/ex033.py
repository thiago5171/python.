"""
ESSE QUESTAO É IGUAL A QUESTAO 7

faça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for
"""
v = int(input(" digite um valor para ter sua tabuada: "))
n = 1
while n<11:
     print("{} x {} = {} ".format(v,n,v*n))
     n = n+1