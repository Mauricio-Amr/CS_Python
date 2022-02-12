from abc import abstractmethod, ABC


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        self.saldo += valor
        self.descricao()

    def descricao(self):
        print(f'Agencia : {self.agencia} \n'
              f'Conta : {self.conta} \n'
              f'Saldo : {self.saldo}\n'
              f'\n')


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.descricao()


class ContaPoupanca(Conta):

    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.descricao()
