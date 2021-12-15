class Pessoa:
    ano = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano - self.idade)

    @classmethod # decorador de metodo para classe
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano - ano_nascimento
        return cls(nome , idade)