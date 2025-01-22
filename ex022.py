nome = str(input('Digite seu nome: ')).strip()
print ('Análisando seu nome...')
print ('Seu nome em maiúsculo é: {}'.format (nome.upper())) 
print ('Seu nome em minúsculas é: {}'.format(nome.lower())) 
print ('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count (' ')))
separar = nome.split() #pra separar todas as palavras inseridas
print ('Seu primeiro nome é {} e ele tem {} letras'.format(separar[0], len(separar[0])))

#deu dor de cabeça com alguns erros