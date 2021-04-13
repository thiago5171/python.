""" A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [-10, -8, 0, 1, 2, 5, -2, -4]. Mostre a menor e a maior temperatura, assim como 
a temperatura média. A lista de temperaturas de Mons, na Bélgica, foi armazenada na 
lista T = [-10, -8, 0, 1, 2, 5, -2, -4]. Mostre a menor e a maior temperatura, assim como a temperatura média.
 """
t = [-10, -8, 0, 1, 2, 5, -2, -4]
maior= menor= soma = media = cont = n = 0

for i in range(0,len(t),1):
    if i==0 :
        maior=t[i]
        menor=t[i]
    
  
    if (t[i]) < menor:
        menor=t[i]

    if t[i]>maior:
        menor=t[i]

for i in t:
    soma = soma + i
    cont+=1
media = soma/cont


print(f"maior temperatura->{maior}\n",
f"menor temperatura->{menor}\n"
f"tempreatura media->{media:.2f}" )     