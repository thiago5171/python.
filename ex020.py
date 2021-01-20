#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas 
#podem ou não formar um triângulo
print("digite os 3 lados de um triangulo: ")
a = int(input())
b = int(input())
c = int(input())

# a condição de existencia de um triangulo é que a soma dos dois lado sejam maior que o lado restante
if (a+b > c) and (a+c > b) and (b+c > a):
    print("é possiver formar um triangulo com essas retas!")
else:
    print("essas retas nao podem formar um triangulo!")