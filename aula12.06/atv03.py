#crie um cadastro de clientes que receba: nome, idade, dada de aniversario e endereço completo. add em um dicionario, imprima no final
name = input('Informe o seu nome: ')
idade = int(input('Informe sua idade: '))
data_aniverario = input('Informe sua data de aniversario DIA/MÊS/ANO: ')
endereco_rua = input('Informe sua rua: ')
endereco_num = input('Informe o seu numero de endereço: ')
endereco_bairro = input('Informe o seu bairro: ')

cadastro = {'nome':name,
            'idade':idade,
            'Data de Aniversario':data_aniverario,
            'Rua':endereco_rua,
            'Número': endereco_num,
            'Bairro':endereco_bairro,

}

print(cadastro)


