def aumPerc(valor, aumento):
    perc = aumento / 100
    soma = valor + (valor*perc)
    return soma

vl = int(input('Digite o valor : '))
aumento = int(input('Digite a percentagem : '))

print(aumPerc(vl, aumento))