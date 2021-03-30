""" Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, mês e ano para 3 variáveis inteiras.
 Antes disso, verifique se as barras estão no lugar certo, e se DD, MM e AAAA são numéricos.
"""
teste=False
cadeia= input("insira uma data no formto “DD/MM/AAAA”: ")

numericos= cadeia.split("/")# divide a string onde tem / gerando uma lista

numericos = "".join(numericos)#junta a lista


teste = numericos.isdigit()#verifica se todos valores sao digitos
print(cadeia)
if  (cadeia[2]=="/"  and cadeia[5]=="/"):
    if teste==True:
        dia=int(cadeia[:2])
        mes= int(cadeia[3:5])
        ano= int(cadeia[6:]) 
        print(f"dia->{dia} \nmes->{mes} \nano->{ano}\n")
else:
    print("\nERRO, \nas barras ""/"" não foram inseridar \nou \nos valores nao foram digitado numericos no local correto ")
