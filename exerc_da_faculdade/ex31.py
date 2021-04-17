"""Percorra duas matrizes/listas e gere uma terceira sem elementos repetidos."""

lista2=[0,0,0,0,0]
lista1=[0,0,0,0,0]
lista10=[0,0,0,0,0]
c1=c2=c3=0

for i in range(0,5,1):
    lista1[i]=int(input(f"digite o item {i} da lista 1: "))

print(" ")

for i in range(0,5,1):
    lista2[i]=int(input(f"digite o item {i} da lista 2: "))

lista10=lista1[:]
for i in range(0,5,1):
    if lista1[i]  in lista2:
        del(lista10[i])
        lista10.append(0)
        c1+=1
        
    print(lista10[i],i)
for i in range(4,5-(c1+1),-1):
    print(f"{i}",end=' ')
print(lista10,lista1,lista2)


        
