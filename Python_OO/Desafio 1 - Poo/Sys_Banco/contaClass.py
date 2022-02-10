from abc import abstractmethod, ABC

class Pessoa:
    def __init__(self, nome, idade):
        self._nome=nome
        self._idade=idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

class Cliente(Pessoa):
     def __init__(self, nome,idade):
         super().__init__(nome, idade)
         self.conta= None

     def inserir_conta(self,conta):
         self.conta = conta

class Conta(ABC):
    def __init__(self, agencia , conta, saldo):
        self.agente = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        pass


    def deposito(self, valor):
       self.saldo += valor
       self.descricao()


    def descricao(self):
        print(f'Agencia : {self.agencia}'
            f'Conta : {self.conta}'
            f'Saldo : {self.saldo}')



class ContaCorrente(Conta):
    def __init__(self,agencia, conta, saldo, limite =100):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.limite = limite

    def sacar(self,valor):

        self.saldo -= valor
        self.descricao()

class ContaPoupanca(Conta):
    pass