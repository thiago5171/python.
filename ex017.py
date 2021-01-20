# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input("digite o  ano para saber se ele eh bissexto: "))

""" passos para saber se um ano é bissexto
1)
Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
2)
Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
3)
Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.
"""
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0 :
    print("o ano de  {} é bissexto.".format(ano))
else:
    print("o ano de {} não é bissexto.".format(ano))

"""
tambem é possivel atraves da biblioteca "determine" é possivel pegar o ano atual  da maquina
from datetime import date
ano = date.today().year
print(ano)
"""