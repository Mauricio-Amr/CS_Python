class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeDaClasse =self.__class__.__name__

    def falar(self):
        print(f'{self.nomeDaClasse} esta falando ...')


class Cliente(Pessoa) :

    def comprar(self):
        print(f'{self.nomeDaClasse} esta comprando')

class Aluno(Pessoa):

    def estudando(self):
        print(f'{self.nomeDaClasse} esta estudando')
