""". Faça um programa que leia vários conjuntos de três valores reais e mostre para cada
conjunto: sua soma, seu produto e sua média. O programa para quando um conjunto não
entrar com seus valores em ordem crescente."""
soma = media= produto = cont=0
while True:
    a= float(input("a = "))
    b= float(input("b = "))
    c= float(input("c = "))
    if a<b<c:
        break
    else:
        soma= a+b+c
        media= soma/3
        produto=a*b*c
        print("=-="*7)
        print(f"a soma foi {soma} ")
        print(f"a media foi {media:.2f}")
        print(f"o produto foi{produto}")
        print("=-="*7)
print("FIM")
    
