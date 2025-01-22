salario =float(input('Qual o salário do funcionário?R$'))
novo = salario + (salario * 15 / 100)
print('Um fucionário que ganhava R${:.2f}, com 15% de aumento passa a ganhar R${:.2f}'
      .format(salario, novo))

#acho que peguei a manha do .format aqui