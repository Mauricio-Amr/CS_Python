class Pessoa :
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):

    def cliente(self):
        self.nome =self.nome


    @property
    def nome(self):
        return self.nome

    @property
    def idade(self):
        return self.idade