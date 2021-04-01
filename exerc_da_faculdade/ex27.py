"""Leia uma string contendo letras de uma frase inclusive os espaços em branco. 
Retirar os espaços em branco e depois escrever o vetor resultante.
"""
string = input("digite letras de uma frase inclusive os espaços em branco:\n").split()
string= "".join(string)
print("=-="*10)
print(string)
print("=-="*10)
