"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a
sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar 
ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta 
ou que passou do prazo.
"""

ano = int(input("digite seu ano de nascimento"))

idade = 2021 - ano
anoa = ano + 18
print("quem nasceu em {} tem {} anos  em 2021".format(ano,idade) )
if idade == 18 :
    print("voce tem que se alistar IMEDIATAMENTE!")
elif idade > 18 :
    alistam = idade - 18
    print("voce ja deveria ter se alistado há {} anos".format(alistam))
    print("seu alistamento foi em ",anoa)
else:
    alistam = 18 - idade
    print("faltam {} para seu alistamento".format(alistam))
    print("seu alistamneto sera em ",anoa)


