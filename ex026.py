frase = str(input('Digite uma frase:')).strip().upper()
print ('A letra A aparece {} vezes na frase.'.format(frase.count('A'))) #conta quantos A tem na frase
print ('A primeira letra A apareceu na posição {}'.format(frase.find('A'))) 
print ('A ultima letra A apareceu na posição {}'.format(frase.rfind('A'))) #encontra pela direita