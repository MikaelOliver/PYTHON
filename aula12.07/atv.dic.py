#faça um quiz usando o discionario com as seguintes chaves: PERGUNTA, OPÇÕES, RESPOSTAS
#faça a validação da opção escolhida com a resposta e imprima.

quis_dic = {
    'pergunta':['QUANTO É 2 + 2? ','QUANTO É 7 + 7','QUANTO É 5 + 5',],
    'opções':[[1,2,3,4],[14,15,16],[10,11,12]],
    'resposta': [4,14,10] 
}
print('='*30)
print('BEM VINDO AO QUIS DO VALLEY')
print('='*30)
print(quis_dic['pergunta'][0])
print(f'AS OPÇÕES SÃO: {quis_dic["opções"][0]}')
usuario_resposta = int(input('INFORME SUA RESPOSTA: '))
pontuação = 0

if usuario_resposta == quis_dic['resposta'][0]:
    print('PARABENS VOCÊ ACERTOU👌')
    pontuação +=1
else:
    print(f'RESPOSTA ERRADA.')


print(quis_dic['pergunta'][1])
print(f'AS OPÇÕES SÃO: {quis_dic["opções"][1]}')
usuario_resposta = int(input('INFORME SUA RESPOSTA: '))
if usuario_resposta == quis_dic['resposta'][1]:
    print('PARABENS VOCÊ ACERTOU')
    pontuação +=1
else:
    print(f'RESPOSTA ERRADA.')
    
print(quis_dic['pergunta'][2])
print(f'AS OPÇÕES SÃO: {quis_dic["opções"][2]}')
usuario_resposta = int(input('INFORME SUA RESPOSTA: '))
if usuario_resposta == quis_dic['resposta'][2]:
    print('PARABENS VOCÊ ACERTOU')
    pontuação +=1
else:
    print(f'RESPOSTA ERRADA.')
print('='*30)
print(f'A SUA PONTUAÇÃO FOI: {pontuação}')
        




