from banco import Banco
from conta import Conta
from abc import abstractmethod

class ContaCorrente(Conta):
    def sacar(self, valor):
        self._saldo -= valor


