#formação de triângulos.


print ('-=-' * 20)
print ('Analisador de triângulos...')
print ('-=-' * 20)

r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print ('Os seguimentos acima podem formar um triângulo.')
else:
    print ('Os seguimentos acima não podem formar um triângulo.')