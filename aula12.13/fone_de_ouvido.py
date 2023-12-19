class foneDeOuvido():
    def get_volume(self):
        print('ENTREI NO GET')
        return self.__volume
    def set_volume(self,novo_volume):
        print('ENTREI NO SET')
        self.__volume = novo_volume
    
    volume = property(get_volume, set_volume)

fone = foneDeOuvido()

fone.set_volume = input('Qual volume? ')
print(f'O fone ta no volume: {fone.set_volume}')
fone.volume = input('Qual volume? ')
print(f'O fone ta no volume: {fone.volume}')