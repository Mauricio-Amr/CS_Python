''' Herança multiplas '''


class A:
    def falar(self):
        print('falando ... estou em A')

class B(A):
    def falar(self):
        print('falando ...estou em B')

class C(A):
    def falar(self):
        print('falando ... estou em C ')

class D(B, C): #assume a herança da esquerda para a direita
    pass


d =D()

d.falar()