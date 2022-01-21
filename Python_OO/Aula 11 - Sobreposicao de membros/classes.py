class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeClasse} falando ...')

class  Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeClasse} comprando ...')

    def falar(self):
        print(f'Cliente {self.nomeClasse} falando ...')

class ClienteVip(Cliente):
    
    def __init__(self, nome , idade, sobrenome):
        Pessoa.__init__(self, nome , idade)
        self.sobrenome = sobrenome

    
    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')
        '''  super().falar()
        print(f'Outra coisa')'''