#estruturas condicionais
variavel = 20
if variavel < 20:
    print('menor que 20')
elif variavel == 20:
    print('igual a 20')
elif variavel > 20 and variavel < 50:
    print('esta no intervalo entre 21 e 49')
else:
    print('qualquer outra coisa')


# estruturas de repetição
# FOR e WHILE
# FOR sempre vai querer um intervel
for i in range(1,11, 2):
    print(i)


contador = 5

while contador > 0:
    print(f'esse é o print do numero: {contador}')
    contador -=1


#join - para unir strings.
lista = ['João','Paulo','II']
nome = ' '.join(lista)
print(nome)