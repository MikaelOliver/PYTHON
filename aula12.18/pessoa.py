class Pessoa:
    nome = 'Mikael'
    def __str__(self):
        return f'O seu nome é: {self.nome}'


class Empregado(Pessoa):
    cargo = 'Colaborador'
    salario = 1.320

class Estudante(Pessoa):
    matricula = 23456
    def __str__(self):
        return f'para acessar use a matricula: {self.matricula}.'

class EstudanteGraduacao(Pessoa):
    curso = 'CIENCIAS DA COMPUTACAO'

class EstudantePos(Pessoa):
    nivel = 1
    orientador = 'Prof. Paulo Junior'

    def __str__(self):
        return f'O seu orientador é {self.orientador} e está no nivel {self.nivel}'

print(Pessoa(),Estudante(),EstudantePos())