#count - função é contar quantas vezes um determinado caractere aparece em um string.
#upper and lower - dois metodos que deixam a sting em MAIUSCULA ou a string toda em MINUSCULA
#find - busca por uma expressão dentro da frase.
#replace - É utilizado para realizar alterações dentro das strings.
#capitalize - deixa a primeira letra da frase maiusculas.
#split - transforma a sua string em uma lista.
frase = 'A banana é a amerela e o abacate é verde'.lower()
letra = 'a'
print(f'a letra " {letra} " aparece  {frase.count(letra)} vezes na frase "{frase}"')
achei = frase.find('ana')
if achei >= 0:
    print(f'A expressão foi encontrada no indice {achei}')
else:
    print(f'A expressão não foi encontrada')

nova_frase = frase.replace('banana', 'maracuja')
nova_frase1 = frase.replace(' ','')
print(frase)
print(nova_frase)
print(nova_frase1)
print(frase.capitalize())
print(frase.split())





# saida = input('digite [S] para sair: ').upper()
# if saida == 'S':
#     print(saida)