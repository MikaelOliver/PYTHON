def gorjeta(valor_gorjeta):
    valor_total = valor_gorjeta * .12
    return valor_total
    

valor_conta = float(input('Difige o valor da conta: '))
valor_total = gorjeta(valor_conta)
print(f'A gorjeta do garçom é: {valor_total:.2f}')