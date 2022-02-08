from banco  import Banco


class Pessoa :
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):

    def cliente(self , agencia ,conta):

        self.agencia = agencia
        self.conta =conta

    @property
    def nome(self):
        return self.nome

    @property
    def idade(self):
        return self.idade




cl = Cliente('maria',19)
print(cl)