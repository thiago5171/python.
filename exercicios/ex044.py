"""Refaça o DESAFIO 035, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
 termos da progressão usando a estrutura while.
"""
print("Gerador de PA")
print("=-="*13)
termo = int(input("digite o primeiro termo da PA: "))
razao = int(input("Digite a razão: "))
cont=1
while cont<=10 :
    print("{} -> ".format(termo), end=' ')  
    termo = termo + razao
    cont +=1

print("Pausa")