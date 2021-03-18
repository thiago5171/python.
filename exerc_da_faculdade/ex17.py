
#soma = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50


e=d=1
soma=0.0
for d in range(d,51,1):
     soma+=e/d
     
     e+=2

print(f"{soma:.2f}" )
