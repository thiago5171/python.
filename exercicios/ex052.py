l=[]

maior=menor=0

maiori=[]
menori=[]
for i in range(0,6):
    l.append(int(input(f"digite o valor da lista no indice {i}: ")))
    

l2=l[:]
l2.sort()
   
menor=l2[0]
maior=l2[5]

for i in range(0,6):
    if maior==l[i]:
        maiori.append(i)

    if menor==l[i]:
        menori.append(i)
print(f"o maior valor digitado foi {maior} foi nas posições",end=' ')
for i in maiori :
    print(f"{i}",end='...')

print(f"\no menor valor digitado foi {menor} foi nas posições",end=' ')
for i in menori :
    print(f"{i}",end='...')
print("\n")