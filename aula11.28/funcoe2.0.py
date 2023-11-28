def numero_reverso(number):
    # inverse_number = number[::-1]
    # return int(inverse_number)
    reverso = 0
    while number > 0:
        ultimo_valor = number % 10
        reverso = (reverso* 10) + ultimo_valor

        number = number // 10

    return int(reverso)

numero = int(input('Informe um número: '))
resultado = numero_reverso(numero)
print(f'O número informado foi: {numero} e o reverso dele é: {resultado}')