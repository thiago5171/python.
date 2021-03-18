n=int(input("diigte um numero: "))
i=1
soma=0
for i in range(i,n,1):
    if n%i==0:
        soma+=i

if soma==n:
    print("o numero é perfeito ")
else:
    print("o numero NAO é perfeito ")
