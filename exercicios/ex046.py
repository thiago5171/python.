n = int(input("digite ate que que termo a sequencia de fibonacci deseja saber: "))
cont=1
cont2=1

aux2=1
aux1=0
print("0-> 1->", end=' ')
while cont <= n-2:
   
    aux3 = aux1+aux2

    print("{}-> ".format(aux3), end=' ')
       
    aux1 = aux2
    aux2 = aux3

    cont +=1
print("FIM")    