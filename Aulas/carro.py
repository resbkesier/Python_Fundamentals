# -*- coding: UTF-8 -*-
# class Automovel():

#     def __init__(self):
#         self.motor = 'Combustão'

#     def ligar(self):
#         print('carro ligado')
 

# class Carro(Automovel):
    

#     def __init__(self):
#         Automovel.__init__(self)
#         self.rodas = 4
#         self.porta_mala = 'Normal'
#         self.volante = True
#         self.tanque = True

    
#     def desligar(self):
#         print('carro desligado')

#     def acelerar(self):
#         print('acelerando')

#     def frear(self):
#         print('freando')

# class Fiat147(Carro):

#     def __init__(self):
#         Carro.__init__(self)
#         self.motor = 'Eletrico'
#         self.porta_mala = 'Com agua'


# c001 = Fiat147()
# print(c001.motor)


class Pai():
    hobby = 'Programar'
    def __init__(self):
        self.profissao = 'Advogado'

    def mudarProfissao(self, nova_profissao):
        self.profissao = nova_profissao

    def mudarHobby(self):
        self.hobby = 'Jardineiro'


joao = Pai()

joao.mudarProfissao('Carpinteiro')
joao.mudarHobby()
print(joao.hobby)








class Mae():
    hobby = 'vender miçanga'
    
    def __init__(self):
        self.profissao = 'medica'
        


class Filho(Pai, Mae):

    def __init__(self):
        Mae.__init__(self)
        # self.profissao = 'Programador'
    

# jose = Filho()

# # print(jose.hobby)

# maria = Mae()

# print(maria.hobby)