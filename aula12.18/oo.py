class Estudante:
    nome = 'Paulo'
    matricula = 353637

class EstudanteGraduacao(Estudante):
    curso = 'ADS'

class EstudantePos(Estudante):
    nivel = 1
    orientador = 'Prof Carlos Alberto'



aluno = EstudanteGraduacao()
print(f'Olá, {aluno.nome} seu curso de graduação é {aluno.curso} e sua matricula de acesso é {aluno.matricula}')


aluno2 = EstudantePos()
print(f'\nOlá, {aluno2.nome} seu nivel é {aluno2.nivel} e Tutor será o {aluno2.orientador} para seu acesso ultilize a matricula {aluno2.matricula}')