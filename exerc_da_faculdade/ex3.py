"""Desenvolva  um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a 
percorrer e a velocidade média esperada para a viagem."""
distancia = float(input("digite a distancia que ira ser percorrida: "))

velocidade = float(input("digite a velocidade média esperada para a viagem: "))

tm= distancia/ velocidade

print(f"ao tempo médio da viagem foi de {tm:.2f}km/h")