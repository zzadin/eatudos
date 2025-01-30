#calculando preço por km com descontos..
distancia = float(input('qual a distância da sua viagem?'))
print ('você está prestes a começar sua viagem de {}km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print ('e o preço da sua passagem será de R${:.2f}'.format(preço))