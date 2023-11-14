l1 = str(input('digite uma letra: '))
l2 = str(input('digite uma letra: '))
l3 = str(input('digite uma letra: '))
l4 = str(input('digite uma letra: '))
l5 = str(input('digite uma letra: '))
lista_consoante = []
if l1 != 'a' and l1 != 'e' and l1 != 'i' and l1 != 'o' and l1 != 'u':
    print('É uma consoante')
    lista_consoante = [l1]
if l2 != 'a' and l2 != 'e' and l2 != 'i' and l2 != 'o' and l2 != 'u':
    print('É uma consoante')
    lista_consoante.append(l2)
if l3 != 'a' and l3 != 'e' and l3 != 'i' and l3 != 'o' and l3 != 'u':
    print('É uma consoante')
    lista_consoante.append(l3)
if l4 != 'a' and l4 != 'e' and l4 != 'i' and l4 != 'o' and l4 != 'u':
    print('É uma consoante')
    lista_consoante.append(l4)
if l5 != 'a' and l5 != 'e' and l5 != 'i' and l5 != 'o' and l5 != 'u':
    print('É uma consoante')
    lista_consoante.append(l5)
print(lista_consoante)