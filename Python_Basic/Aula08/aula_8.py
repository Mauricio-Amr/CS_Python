nome = input('Qual o seu nome ? ')#input sempre retorna str
#print(f'o usuario digito {nome}'
 #     f' e o tipo de variavel é {type(nome)}')

idade = input('Qual a sua idade ? ')
anos_nas = 2021 - int(idade)

print()
print(f'{nome} tem {idade} anos.\n'
      f'{nome} nasceu em {anos_nas}')

#calculadora
numero_1 = int(input('digite um numero : '))
numero_2 = input('digite outro numero : ')
numero_2 = int(numero_2)

print (numero_1 + numero_2)
