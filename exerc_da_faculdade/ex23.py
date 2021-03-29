"""Determinar quantas vogais tem dentro de uma determinada string dada e imprimir a string sem as vogais."""
nome = input("->")
cont = len(nome)
cont1=i=j=0
semvogais= nome 
vogais="aeiou"
for i in range(0,cont,1):
    if vogais[i]in nome:
        cont1+=1
        continue
    semvogais[j]=nome[i]
    j+=1    
    
print(cont1,"\n",semvogais)