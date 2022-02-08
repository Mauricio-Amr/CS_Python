from banco import Banco
from abc import abstractmethod

class ContaCorrente(Banco):

    def __init__(self, num_conta, num_agencia):
        self.num_conta = num_conta
        self.num_agencia = num_agencia
        self.saldo =saldo

    def depositar(self, valor):
        self.conta += valor

    @abstractmethod
    def sacar(self, valor):
        valor

    def saldo_cc(self):
        print(f'{self.num_agencia} - {self.num_conta}')
        print(f'saldo em conta : {self.conta}')
