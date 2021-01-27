#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input("digite o valor da largura: "))
altura = float(input("digite o valor da altura: "))
# descobrir a  area
metrosquad = altura * largura
# calcular  qunatos  de tinta foi usada
tinta = metrosquad/2

print("sua parede tem a dimensao  {}x{}  e sua area eh {:.2f}.".format(largura,altura,metrosquad))
print("para pintar sua parede sera necessario  {:.2f}l de tinta".format(tinta))