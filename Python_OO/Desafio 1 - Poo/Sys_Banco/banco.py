class Banco :
    def __init__(self,conta, agencia):
        self.conta = conta
        self.agencia = agencia

    @property
    def conta(self):
        return self.conta

    @property
    def agencia(self):
        return self.agencia