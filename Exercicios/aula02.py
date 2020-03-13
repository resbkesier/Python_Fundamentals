from functools import reduce
# # Dada o dicionario:
# import json
# produtos = dict(produtos=dict(p1=dict(nome="Camiseta Star Wars", preco=99.90),
#                               p2=dict(nome='Caneca Ricky&Morty', preco=49.90),
#                               p3=dict(nome='Camiseta SpiderMan', preco=69.90)))

# teste=json.dumps(produtos)
# teste2=json.loads(teste)
# # Apartir do id do produto mostraremos o nome e o preco
# # Caso o produto não exista mostraremos a seguinte mensagem
# # Produto inexistente

# # try:
# #     id_produto = input('Digite o ID do produto: ')
# #     if id_produto not in produtos['produtos']:
# #         raise ValueError('Produto Inexistente!')
# #     else:
# #         nome = produtos['produtos'][id_produto]['nome']
# #         preco = produtos['produtos'][id_produto]['preco'])
# #         # print('Preco %s' %preco)
# #         print(f"Produto: {nome}")
# #         print("Preço: {}".format(preco))

# # except ValueError as v:
# #     print(f'Erro: {v}')

# print(type(teste))

# print('-'*30)

# print(type(teste2))

# with open('novo_arquivo', '+') as f:
#     f.write('\nMeu primeiro arquivo')
# #     f.read()

# # def dobra(valor):
# #     return valor * 2

# # print(dobra(122))


# # produtos = []
# # def cadastraProduto(produto):
# #     return produtos.append(produto)

# # def listaProdutos():
# #     print(produtos)

# # def deletaProduto(produto):
# #     if produto in produtos:
# #         produtos.remove(produto)
# #     else:
# #         print('Produto inexistente')

# # cadastraProduto('Tenis')
# # cadastraProduto('Sapato')
# # cadastraProduto('Calca')


# # listaProdutos()

# # deletaProduto('Sapato')

# # listaProdutos()


# # nome = 'python'

# # def linux():
# #     global nome
# #     nome = 'linux'
# #     return nome

# # linux()
# # print(nome)

# # def teste(produto: str) -> list:
# #     print(var)


# # teste()
# # usuarios = []

# # def cadastra_Pessoa(add=None):
# #     # pessoa = dict(nome='Renato', sobrenome='Barbosa', idade=26)
# #     if add is None:
# #         pass
# #     else:
# #         usuarios.append(add)

# # cadastra_Pessoa('Renato')
# # cadastra_Pessoa('Mario')
# # print(usuarios)

# # frutas = []


# # def inserFrutas(*args):
# #     for f in args:
# #         frutas.append(f)


# # inserFrutas('abacaxi', 'laranja', 'limão', 'banana')

# # print(frutas)

# camisetas = {}

# def insereCamiseta(**kwargs):
#     global camisetas
#     camisetas = kwargs
#     return camisetas

# insereCamiseta(camiseta01='Star Wars', camiseta02='Batman')
# print(camisetas)

# print('')

# dobro = lambda x: x * 2

# print(dobro(10))

# Faça uma função lambda que receba 3 valores e retorne a soma

# soma = lambda x , y, z: x + y + z

# print(soma(10,15,10))


# numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# dobro = tuple(map(lambda x: 1, numeros))
# numeros_par = list(filter(lambda x: x % 2 == 0, numeros))
# soma1 = reduce(lambda x, y: x + y, numeros)
# soma2 = reduce(lambda x, y: x + y, dobro)
# soma3 = reduce(lambda x, y: x + y, numeros_par)
# # print(dobro)
# print(dobro)
# for i in numeros:
#     dobro.append(i*2)
# n = []
# for i in numeros:
#     if i % 2 == 0:
#         n.append(i)