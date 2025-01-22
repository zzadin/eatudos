#sorteio de nomes
import random 
a1 = str(input(' DIGITE O NOME DE UM ALUNO: '))
a2 = str(input(' DIGITE O NOME DE UM ALUNO: '))
a3 = str(input(' DIGITE O NOME DE UM ALUNO: '))
a4 = str(input(' DIGITE O NOME DE UM ALUNO: '))
lista = ( a1, a2, a3, a4)
print ('os alunos a serem sorteados são', lista)
sorteio = random.choice (lista)

print ('O aluno sorteado foi:' ,sorteio)
