""" Desenvolva em cada LP um programa que leia um número e verifique se é ou não um número primo.
Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números 
ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. 
Observe que o 0 e 1 não são primos e que 2 é o único número primo que é par."""
cont= 0
n=int(input("Digite um numero:"))

for i in range(2,n,2):
    if i==2:
        if n%2==0:
            print("numero não é primo")
            break
    else:
        i-=1
        # Se o resto da divisão for zero o número não é primo
        if (n%i==0):
            cont+=1
if cont==0:
    print("numero é primo")
else:
    print("numero não é primo")

