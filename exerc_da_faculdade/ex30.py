"""Ler duas matrizes/listas e gere uma terceira com os elementos das duas primeiras.
"""
lista=lista2=lista1=[0,0,0,0,0]

for i in range(0,5,1):
    lista1[i]=int(input(f"digite o item {i} da lista 1: "))

for i in range(0,5,1):
    lista2[i]=int(input(f"digite o item {i} da lista 2: "))

lista= lista2+lista1

for i1,i in enumerate(lista):
    print(f"item {i1} da lista geral->{i} ")