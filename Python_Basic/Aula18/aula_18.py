'''
While / else
contadores
acumuladores
'''

contador = 1
acumulador = 1

while contador <= 10:

    print(f'{contador} : {acumulador}')

    if contador > 5:
        break
    acumulador = acumulador + contador
    contador += 1

else:
    print('chego no else')

print('isso sera executado')