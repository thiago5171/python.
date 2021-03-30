"""Receba do usuário uma string S, um caractere C, e uma posição P e devolva o ı́ndice da primeira posição 
da string onde foi encontrado o caractere C. A procura deve começar a partir da posição P.
"""
cont=i=0
verificador=False
s=input("digite uma string:\n").upper()

# while para verificar se tem apenas um caractere
while True:
    c=input("digite um caractere:\n").upper()
    if len(c)>1 or  len(c)<0 :
        print("Erro!, digite apenas um caractere")
        continue
    else:
        break


p =int(input(f"digite um indice  de 0 até {len(s)-1}: "))

for i in range(p,len(s)): 
    
    if s[i]==c:
        print(f"o  caractere foi encontrado no indice {i}")
        verificador=True
        break

    
if verificador == False:
    print("\ INDICE NAO ENCONTRADO\n ")
