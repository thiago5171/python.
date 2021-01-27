""")A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""
ano = int(input("digite o seu ano de nascimento: "))
#TROQUE O ANO 2021 PARA O ATUAL PARA, CASO FOR COPIAR
idade = 2021-ano

print("sua categoria é ...")
if idade<10:
    print("MIRIM")
elif (idade>9 and idade < 15):
    print("INFANTIL")
elif (idade>14 and  idade<20):
    print("JUNIOR")
elif(idade >19 and idade<26):
    print("SENIOR")
else:
    print("MASTER")
