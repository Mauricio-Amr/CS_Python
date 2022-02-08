class Pessoa:

    def __init__(self):
        self.atributo = ''

    @property
    def nome(self):
        return 'Mauricio Amaral'

    @nome.setter
    def nome(self,nome):
        self.atributo = nome


p1 = Pessoa()
p1.nome ='Joao'
print((p1.atributo))
print(p1.nome)
