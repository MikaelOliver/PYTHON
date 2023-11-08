nome = "Mikael"
altura = 1.78
peso = 75
imc = peso / (altura * altura)

# A reposta dessa questão deve ser:
#Fulano tem alt de AlTURA, pesa PES quilos e o seu IMC é: 
#valor
print(nome, "tem", altura, "de altura," )
print("pesa", peso, "quilos e seu IMC é:")
print(imc)

#interpolação

print(f'{nome},tem {altura} de altura, pesa {peso} quilos e o seu imc é:')
print(f'{imc:.2f}')