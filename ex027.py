"""Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
"""
print("digite os 3 lados de um triangulo: ")
a = int(input())
b = int(input())
c = int(input())

# a condição de existencia de um triangulo é que a soma dos dois lado sejam maior que o lado restante
if (a+b > c) and (a+c > b) and (b+c > a):
    print("é possiver formar um triangulo com essas retas!")
    if (a==b==c):
        print("e esse triangulo é um Equilatero")
    elif (a==b or a==c or b==c):
         print("e esse triangulo é um Isosceles")
    else:
        print("e esse triangulo é um Escaleno")

else:
    print("essas retas nao podem formar um triangulo!")
  
  