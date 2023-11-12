#Outra forma de INTERPOLAR
nome = "Geisa"
salario = 4500.99
print(nome, "ganha um salário de R$", salario)
print('='*20)
print(f'{nome} ganha um salário de R${salario}')
print('='*20)
#forma FORMAT de imprimir
#s -string
#d e i - int
#f - float
#x e X - hexadecimais
print('O salário de %s é R$ %.2f' %(nome,salario))