number1 = int(input('digite um número: '))
number2 = int(input('digite um número: '))
number3 = number1 + 1
if number1> number2:
    number1, number2 = number2, number1
    number3 = number1 +1
for i in range(number3, number2):
    print(i)