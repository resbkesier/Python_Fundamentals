# Crie uma classe Mamifero com os atributos:
#      bebe leite

# Crie uma classe homosapiens com os atributos:
#   
#   polegares = True
#   formaCaminhar = 'Bipede'
# Métodos:
#    Caça
#    Comer
#    Dormir
#    Construir


class Mamifero():
    def __init__(self):
        self.bebe_leite =  'Sim'



class Homosapiens(Mamifero):

    def __init__(self):
        super().__init__()
        self.polegares = True
        self.formaCaminhar = 'Bipéde'
    
    def cacar(self):
        print('Caçando...')

    def comer(self):
        print('Comendo...')
    
    def dormir(self):
        print('dormindo...')


jubileu = Homosapiens()
jubileu.comer()
jubileu.dormir()
jubileu.cacar()
print(jubileu.polegares)
print(jubileu.formaCaminhar)
print(jubileu.bebe_leite)







