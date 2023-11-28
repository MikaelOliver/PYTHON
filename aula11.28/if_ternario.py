# condição ternaria aconte em formato de linha.

salario = float(input('Informe o valor do seu sálario: '))
if salario >= 2500.00:
    print('IR será cobrado')
else:
    print('IR não será cobrado')

variavel_controle = 'IR será cobrado' if salario == 2500.00 else 'IR não sera cobrado'
print(variavel_controle)

vr_controll = 'Ok 1' if True else 'Ok 2'