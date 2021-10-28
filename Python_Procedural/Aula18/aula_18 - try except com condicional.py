def converter_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError as error:
        pass



numero = converter_numero(input('digite um numero : '))
print(numero * 5)