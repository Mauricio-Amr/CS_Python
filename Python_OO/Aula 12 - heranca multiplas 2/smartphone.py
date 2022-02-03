from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self.conectado = False

    def conectar(self):
        if not self._ligado:
            info= f'{self._nome} não esta ligado'
            print(info)
            self.log_erro(info)
            return

        if self.conectado:
            erro = f'{self._nome} JA ESTA CONECTADO !!!'
            print(erro)
            self.log_erro(erro)
            return

        info = f'{self._nome} ESTA CONECTADO'
        print(info)
        self.log_info(info)
        self.conectado = True


    def desconectar(self):
        if not self.conectado:
            erro =f'{self._nome}NÃO ESTA CONECTADO'
            print(erro)
            self.log_erro(erro)
            return

        info = f'{self._nome} foi desligado com sucesso'
        print(info)
        self.log_info(info)
        self.conectado = False
