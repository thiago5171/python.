n= str(input("digite uma frase/palavra ")).upper().strip()
d=n.split()
j= ''.join(d)
inver= ''
for i in range(len(j)-1,-1,-1):
    inver+=j[i]

if n==inver:
    print("a frase é um palindromo")
else:
    print("a frase não é um palindromo")

