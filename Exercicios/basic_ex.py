# Faça um script que peça o seu nome
# e imprima a seguinte saudação
# Ola meu nome é nome

# nome = input('Digite seu nome: ')
# print('Meu nome é', nome)

# Dado a lista:



# times = [['Corinthians', 'Palmeiras', 'São Paulo'], ['Preto', 'Branco', 'Verde', 'Vermelho']]

# imprima na tela as seguintes mensagens:

# time: <nome_time>, cores: <cores_time>

# for i in times[0]:
#     for n in times[1]:
#         if times[0][0] == 'Corinthians':
#             cor1, cor2 = 'Preto', 'Branco'
#             print(f'time: {i} Cores: {cor1} {cor2}')





# print('time:', times[0][0], 'cores:', times[1][0], times[1][1])
# print('time: {} Cores: {} {}'.format(times[0][1], times[1][2], times[1][1]))
# print(f'time: {times[0][2]} Cores: {times[1][0]} {times[1][1]} {times[1][3]}')
# dado o dicionario:

dados = {
    'estados' : {
        'sp': {
            'nome': 'São Paulo',
            'municipios': 645,
            'populacao': 44.04
        },
        'rj': {
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'populacao': 16.72
        },
        'mg': {
            'nome': 'Minas Gerais',
            'municipios': 31,
            'populacao': 20.87
        }
    }
}

# Imprima na tela as seguintes mensagens:

# Estado: <nome_estado>
# Municipios: <qnt_municipios>
# Populacao: <qnt_populacao>


# print(f"Estado: {dados['estados']['sp']['nome']}")
# print(f"Municipios: {dados['estados']['sp']['municipios']}")
# print(f"População: {dados['estados']['sp']['populacao']}")

# print(f"Estado: {dados['estados']['rj']['nome']} \nMunicipios: {dados['estados']['rj']['municipios']} \nPopulação: {dados['estados']['rj']['populacao']}")

# # for estado in dados['estados'].keys():
# #     print(f"Estado: {dados['estados'][estado]['nome']}")
# #     print(f"Municipios: {dados['estados'][estado]['municipios']}")
# #     print(f"População: {dados['estados'][estado]['populacao']}")
# #     print(' ')



# # Faça um programa que receba 4 notas de aluno:

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# n3 = float(input('Digite a terceira nota: '))
# n4 = float(input('Digite a quarta nota: '))

# media_final = (n1+n2+n3+n4)/4

# if media_final >= 7:
#     print(f'Média: {media_final}')
#     print('Aluno Aprovado')

# elif media_final >= 5 and media_final < 7:
#     print(f'Média: {media_final}')
#     print('Aluno Em Recuperação')
# else:
#     print(f'Média: {media_final}')
#     print('Aluno Reprovado')

# calcule a média
# caso seja menor que 7 imprima "Reprovado"
# caso seja maior ou igual que 5 e menor 7 imprima "Recuperação"
# caso contrário imprima "Aprovado"

# Faça um programa que receba dois valores e retorne o maior
# caso sejam igual imprima "valores iguais"


v1 = float(input('Digite o valor 1: '))
v2 = float(input('Digite o valor 2: '))


if v1 == v2:
    print('Valores Iguais')
else:
    print(max(v1, v2))




print(f'teste {v2}')






















