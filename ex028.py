#jogo de adivinhação 1.0
from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador sortear um numero
print ('-=-' * 20)  
print ('vou pensar em um número entre 0 e 5. tente adivinhar...')
print ('-=-' * 20)
jogador = int(input('em que número eu pensei? ')) #jogador tenta adivinhar
print ('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print ('parabéns! você conseguiu me vencer.')
else:
    print ('ganhei! eu pensei no número {} e não no {}'.format(computador, jogador))