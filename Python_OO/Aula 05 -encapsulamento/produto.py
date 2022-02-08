"""
public, protected, private
_ protected
__ private
"""

class  BancoDeDados:

    def __init__(self):
        self.__dados = {}

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id : nome}
        else:
            self.__dados['clientes'].update({id : nome})

    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_clientes(self, id):
        del self.__dados['clientes'][id]


if __name__ == '__main__':

    bd = BancoDeDados()
    
    bd.inserir_clientes(1, 'Mauricio')
    bd.inserir_clientes(2, 'Julio')
    bd.inserir_clientes(3, 'carlos')
    bd.listar_clientes()
    bd.__dados = 'qualquer coisa '
    print(bd.__dados)
    print(bd._BancoDeDados__dados)
