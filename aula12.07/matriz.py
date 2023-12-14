#matrizes

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9] 
          ]

print(matriz[1][1])

matriz_dic ={'inicio':[1, 2, 3],
             'meio':[4, 5, 6],
            'fim':[7, 8, 9] 
          }



class Automovel:
    def __init__(self,placa = 'XX-123'):
        self.placa = placa
    def get_placa(self):
        return self.placa
    def dirigir(self, velocidade):
        print('Estou dirigindo a %d \ km %velocidade')

print(Automovel)