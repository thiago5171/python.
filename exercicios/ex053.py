dicinario =dict()
d=list()
for i in range(0,3,1):
    dicinario["nome"]=input(f"digite o nome de indice[{i}]: ")
    dicinario["idade"]= input(f"digite a idade de indice[{i}]: ")
    
    
    d.append(dicinario.copy())
    
    
for i in range(0,3):
    print(f"{d[i]['nome']}=={d[i]['idade']}")
