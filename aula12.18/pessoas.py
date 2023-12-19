class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.__cpf = None

    
    def get_cpf(self):
        return self.__cpf
    def set_cpf(self,meu_cpf):
        self.__cpf = meu_cpf

class Professor(Pessoa):
    def __init__(self, nome, idade, salario,disciplina,):
        super().__init__(nome, idade)
        self.salario = salario
        self.disciplina = disciplina

    def __str__(self):
        return f'Nome: {self.nome}, idade: {self.idade} e CPF: {self.get_cpf()} salario: {self.salario}, disciplina {self.disciplina}'

class Aluno(Pessoa):
    pass


paulo = Professor('Paulo Junior', 28, 1400.00, 'back-end')
paulo.set_cpf(123456789)
print(paulo)