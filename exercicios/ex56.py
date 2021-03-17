i=1
cont=0
n=int(input())
        
for i in range(i,n+1,1):
    l,c=input().split(" ")
    l=int(l)
    c=int(c)
    if l>c:
        cont+=c
print(cont)
