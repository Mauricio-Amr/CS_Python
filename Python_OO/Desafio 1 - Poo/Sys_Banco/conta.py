from abc import ABC, abstractmethod

class Conta(ABC):

    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo =saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,valor):
        self._saldo = valor

    def depositar(self,valor):

        self._saldo += valor
        self.detalhe()

    def detalhe(self):
        print(f'agencia {self._agencia}')
        print(f'conta {self.conta}')
        print(f'saldo {self._saldo}')