try :
    # a
    # a = []
    # a = {}
    # print(a[1])
    a = 1/0
except NameError as error:
    print('Erro do desenvolvedor , fale com ele ')
except (IndexError,KeyError) as error:
    print('Erro de indice.')
except Exception as error:
    print('Aconteceu um erro inesperado')
else:
    # print('seu programa foi executado com sucesso ')
    # print(a)
    pass
finally:
   # print('Finalmente')
    a = ''

print('Bora continuar')