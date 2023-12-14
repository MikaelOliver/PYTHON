#OBS: GET, SET, COMUNS
#propety - não utiliza o init na class
class Automovel:
    def __init__(self,placa,cor,marca):
        self.__placa = placa
        self.__cor = cor
        self.__marca = marca
    def get_placa(self):
        return self.__placa
    def dirigir(self, velocidade):
        print(f'Estou dirigindo a {velocidade} km/h ')
    def get_cor(self):
        return self.__cor
    def set_cor(self,nova_cor):
        self.__cor = nova_cor
    def get_marca(self):
        return self.__marca

    

carro = Automovel('FDS-2211','Preto','BMW')
print(carro.get_placa())
print(carro.get_cor())
carro.set_cor('Dourado')
print(f'A cor do meu carro é: {carro.get_cor()}')
carro.dirigir(220)
bicicleta = Automovel(None,'PRETO','MONARC')
print(bicicleta.get_cor())
print(bicicleta.get_marca())

# moto = Automovel('MWR-2367')
# print(moto.get_placa())
# moto.dirigir(90)

