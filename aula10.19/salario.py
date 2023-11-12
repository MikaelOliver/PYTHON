salario = float (input( "Digite o seu salário:" ))
reajuste = float(input("Digite o valor de reajuste em % : "))
calc_reajuste = salario * (reajuste / 100)
salario_reajustado = salario + calc_reajuste
print(f'O novo salário com reajuste é R$: {salario_reajustado}')