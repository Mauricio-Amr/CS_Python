class Banco :
    def __init__(self,conta, agencia):
        self._conta = conta
        self._agencia = agencia

    @property
    def conta(self):
        return self._conta

    @property
    def agencia(self):
        return self._agencia