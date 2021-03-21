maior= menor= dg = dp=i =i2= resto1= resto2=0
n,m=input().split(" ")
n=int(n)
m=int(m)

if n>m:
    maior=n
    menor=m
else:
    maior=m
    menor=n

if n==m:
    print(n) 
else:
    i=1
    i2=1
    for i in range(i,maior,1):

        dg= maior/i 
        resto1= maior%i# verificador de resto
        i2=1
#nesse segundo for ele vai pegar a  divisao do menor e comparar com todos os resultados de divisao ate zero  com cada divisao do maior
        for i2 in range(i2,menor,1):

            dp=menor/i2
            resto2= menor%i2
            if dg==dp:
                if (resto1 and resto2)==0:
                    print(dg)
                break
        if dg==dp:
            if (resto1 and resto2)==0:
                break
