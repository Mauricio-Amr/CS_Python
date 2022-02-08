from random import randint

class Pessoa:
    ano = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    #metodo de instacia , necessario  receber o  self
    def get_ano_nascimento(self):
        print(self.ano - self.idade)

    #metodo  de classe , ele precisa estar decorado com @classmethod refere a classe ,global da classe
    @classmethod # decorador de metodo para classe
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano - ano_nascimento
        return cls(nome , idade)

    #metodo estatico como uma função da classe , não pode usa o self , nem a classe
    @staticmethod
    def gerar_id():
        rand= randint(10000,19999)
        return rand

p1 = Pessoa
print(p1.gerar_id())