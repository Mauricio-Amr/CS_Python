# def falaOi():
#     print('oi')
#
# variavel = falaOi
# variavel()

# def master():
#     def slave():
#         print('oi')
#     return slave


def master(func):
    def slave():
        func()
    return slave

def fala_oi():
    print('oi')

variavel = master(fala_oi)
variavel()

#função decoradora é aquela que chama outra função dentro de outra função