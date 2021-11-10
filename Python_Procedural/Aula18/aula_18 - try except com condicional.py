def converter_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError as error:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


while True:
    numero = converter_numero(input('digite um numero : '))
    if numero is None:
        print('Isso não é numero')
    else:
        print(numero * 5)
