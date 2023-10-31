km = float(input("Quantos KM rodados: "))
litros = float(input("Quantos litros de combustível usados: "))
consumo = km/litros
if consumo < 8:
    print("Venda o carro")
elif consumo >= 8 or km <= 14:
    print("Economico")
else:
    print("Super Econimico")