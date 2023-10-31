km = float(input("Quantos KM rodados: "))
litros = float(input("Quantos litros de combustível usados: "))
consumo = km/litros
if consumo < 8:
    print("Venda o carro")
elif consumo >= 8 and consumo <= 14:
    print("Economico")
elif consumo > 14:
    print("Super Econimico")
else:
    print("Consumo não indentificado")