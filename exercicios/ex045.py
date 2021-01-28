"""Melhore o DESAFIO 44, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos
"""
print("Gerador de PA")
print("=-="*13)
termo = int(input("digite o primeiro termo da PA: "))
razao = int(input("Digite a razão: "))
#contador para o programa poder avançar de termo
cont=1
#o mais recebe 10 pois sao os 10 termos pedidos pela questao por padrao
mais=10

total=0
while mais!= 0:  
# esse total vai de inicio receber os 10 primeiros que ele quer do enunciado e depois conforme vai somando 
#apos digitar outro valor para o mais e o segundo while vai dando continuidade pois seu valor vai alterando 
    total = total + mais
    while cont<= total :
        print("{} -> ".format(termo), end=' ')  
        termo = termo + razao
        cont +=1

    print("Pausa...")
    mais=  int(input("mais quantos termos voce quer ver: "))

print("FIM")
print("NO TOTAL FORAM EXIBIDOS {} TERMOS DA PA!".format(total))