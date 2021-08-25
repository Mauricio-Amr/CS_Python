nome = 'Mauricio'  # str
idade = 32  # int
altura = 1.85  # float
e_maior = idade > 18  # bool
peso = 80
imc = peso / (altura ** 2)

print(nome, 'tem ', idade, ' de idade e seu imc é ', imc)
print(f'{nome} tem {idade} de idade e seu é {imc:.2f}')
print ('{} tem {} de idade e seu imc é {:.2f}'.format(nome, idade, imc ))
#para altera a posição use a posição numerica dentro da chave
print ('{0} tem {1} de idade e seu imc é {2:.2f}'.format(nome, idade, imc ))
#pode se usa os valores nomeados
print ('{n} tem {i} de idade e seu imc é {im:.2f}'.format(n=nome,i=idade,im=imc ))

