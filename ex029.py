velocidade = float(input('qual é a velocidade atual do carro? '))
if velocidade > 80:
   print (' \033[31mMultado!! você excedeu o limite permitido de 80km/h.\033[31m')
   multa = (velocidade-80) * 7
   print ('\033[1;31mvocê deve pagar uma multa de R${:.2f}'.format(multa))
print (' \033[32mtenha um bom dia e dirija com segurança.')

