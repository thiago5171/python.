"""Desenvolva em cada LP um programa que exiba uma lista de opções (menu): adição, subtração, divisão, 
multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até a opção saída seja escolhida.
"""
from time import sleep
while True:
    print("\nMenu:\n"
    "1 - adição\n"
    "2 - subtrção\n"
    "3 - divisão\n"
    "4 - multiplicação\n"
    "5 - sair\n")
    n = int(input("Digite a sua opção: "))
    if n==5:
        print("SAIDA CONCLUIDA!")
        break
    elif (n != 1)and (n!=5) and (n !=2)and (n !=3)and (n !=4):
        print("ERRO, digite novamente!!\n")
        sleep(2)
        continue
    else:
        i=0
        v=int(input("digite o valor para saber a tabuada: "))
        print("=-="*7)
        for i in range(1,11,1):
            if n==1:
                print(f"{v} + {i} = {v+i}")
            elif n==2:
                print(f"{v} - {i} = {v-i}")
            elif n==3:
                print(f"{v} / {i} = {v/i}")
            elif n==4:
                print(f"{v} * {i} = {v*i}")
        print("=-="*7)
            
            
