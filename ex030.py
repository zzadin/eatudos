#par ou impar
numero = int(input('digite um numero: '))
resultado = numero % 2
if resultado == 0:
    print (' o número {} é par.'.format(numero))
else:
    print (' o número {} é ímpar.'.format(numero))