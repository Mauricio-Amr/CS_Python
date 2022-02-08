class ContaPoupanca:

    def __init__(self, num_conta, num_agencia, saldo = 100):
        self.num_conta = num_conta
        self.num_agencia = num_agencia
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def saldo_cp(self):
        print(f'{self.num_agencia} - {self.num_conta}')
        print(f'saldo em conta : {self.saldo}')