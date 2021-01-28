"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

x = int(input("digite um numero: "))
y = int(input("digite outro numero: "))
cont = False
while cont == False:
    print("=-="*15)

    opcao = str(input("[ 1 ] somar\n"
    "[ 2 ] multiplicar\n"
    "[ 3 ] maior\n"
    "[ 4 ] novos números\n"
    "[ 5 ] sair do programa\n"
    ">>>>Qual é sua opção? "))
    
    print("=-="*15)
    
    if (opcao == "1"):
        print("a soma entre {} + {} é {} ".format(x,y,x+y))
    elif (opcao=="2"):
        print("a multiplicação entre {} x {} é {} ".format(x,y,x*y))
    elif (opcao=="3"):
        if (x>y):
            print("o maior é {}".format(x))
        else:
            print("o maior é {}".format(y))
    elif(opcao == "4"):
        x = int(input("digite um numero: "))
        y = int(input("digite outro numero: "))
    elif (opcao == "5"):
        cont = True
        print("Finalizando o programa...")
        sleep(2)
    else:
        print("Opcção invalida, digite novamente")
  



print("=-="*15)
print("Fim do programa! Volte Sempre!")
