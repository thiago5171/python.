"""leia um nome completo de pessoa e imprima apenas o nome e sobrenome no formato SOBRENOME/Nome. 
Ex.: Antônio Fernando Silva → SILVA/Antônio
 
"""
nome = input("nome completo:\n").split()
cont= len(nome)-1
nome2= " ".join(nome)
print("\n")
if cont>1: 
    aux=nome[0]
    nome[0]=nome[cont].upper()
    nome[1]=aux
    for i in range(2,len(nome)):
        del(nome[i])

    resume= "/".join(nome)
    print(nome2,"->",resume)


if cont==1:
    aux=nome[0]
    nome[0]=nome[1].upper()
    nome[1]=aux
    resume= "/".join(nome)
    print(nome2,"->",resume)


 