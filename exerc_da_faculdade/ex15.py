n= str(input("digite um valor ")).upper().strip()
d=n.split()
j= ''.join(d)
inver= ''
for i in range(len(j)-1,-1,-1):
    inver+=j[i]

if n==inver:
    print("o valor é um palindromo")
else:
    print("o valor não é um palindromo")

