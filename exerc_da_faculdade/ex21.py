""" EntradaA
 entrada consistira de uma sequ^encia de inteiros que sera terminada quando o valor 0 for 
digitado, o qual n~ao fara parte da sequ^encia.E possvel que a sequ^encia n~ao tenhanenhum numero
 (nesse caso considere 0 como o maior numero da sequ^encia).
 Saida
 Apresente x, y e z, um por linha, onde x,
  y e z representam, respectivamente, a quan-tidade  de  numeros,  o  maior  numero  e  a  media  dos  
  inteiros  da  sequ^encia  com  2  casasdecimais apos a vrgula

z= media 
y=maior
"""
z  = y = soma= 0
x=1 #cont
n=1
print("\n\nDigite os numero, caso queira termina digite (0)")
while n!=0:
    n=int(input("->"))
    if x==1 and n==0:
        break
    
    if (x==1 and n!=0):#quando for a primeira repetição colocar o primeiro valor imputado como o maior
        y=n

    if (y<n and n!=0):# verificar o maior numero
        y=n 
    if n!=0:
        soma+=n
        x+=1
    
x-=1
z= soma/x

print(x)#quantidade 
print(y)#maior
print(f"{z:.2f}")#media



