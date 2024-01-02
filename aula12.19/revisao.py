class Televisao():
    def __init__(self,tamanho):
        self.tamanho = tamanho
        self.canal = 0
        self.ligado = False

    #GETS
    def get_tamanho(self):
        return self.tamanho
    
    def get_canal(self):
        return self.canal
    #SETS
    def set_tamanha(self,novo_tamanho):
        self.tamanho = novo_tamanho
    def set_canal(self,novo_canal):
        if self.ligado == True and novo_canal >= 0 and novo_canal <= 100:
            self.canal = novo_canal
    
    def ligar(self):
        self.ligado = True
        print('Sua TV está ligada!')
    def desligar(self):
        self.ligado = False
        print('Sua TV está desligada!')
        

#chamadas de criação
minha_tv = Televisao(32)
minha_tv.ligar()
minha_tv.set_canal(10)
print(minha_tv.get_canal())
minha_tv.desligar()