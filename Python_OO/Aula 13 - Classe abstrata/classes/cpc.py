from classes.conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo< valor:
            print('Valor insuficiente')
            return

        self._saldo -= valor
        self.detalhe()


