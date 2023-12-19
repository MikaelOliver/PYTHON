#crei abstração para uma super classe funcionario com duas subclasses. imprima todos os dados



class Funcionario:
    def __init__(self,nome,tempo,salario):
        self.nome = nome
        self.tempo = tempo
        self.salario = float(salario)

class Entregador(Funcionario):
    def __init__(self, nome, tempo, salario,setor):
        super().__init__(nome,tempo, salario)
        self.setor = setor

    def get_setor(self):
        return self.setor
    def set_setor(self,setores):
        setores = input('Qual o seu setor? ')
        self.setor = setores

        
    def __str__(self):
        return f'O funcionario: {self.nome} está na empresa à: {self.tempo} anos, com o salario de {self.salario} no setor de {self.setor} '

class Vistoria(Funcionario):
    def __init__(self, nome, tempo, salario,setor):
        super().__init__(nome, tempo, salario)
        self.setor = setor

    def get_setor(self):
        return self.setor
    
    def set_setor(self,setores):
        self.setor = setores

    def __str__(self) -> str:
        return f'O funcionario: {self.nome} está na empresa à: {self.tempo} anos, com o salario de {self.salario} no setor de {self.setor} '

nome = input('Qual o seu nome: ')
tempo_empresa = float(input('Quanto tempo tem de empresa[em anos]: '))
salario = float(input('Qual o seu salário ' ))
setor = input('Qual o seu setor? ')
paulo= Entregador(nome,tempo_empresa,salario,setor)

print(paulo)

pedro = Vistoria(input('Qual o seu nome? ' ),input('Quanto tempo tem na empresa (em anos): '), float(input('Qual o seu salário ' )),input('Qual o seu setor? '))
print(pedro)